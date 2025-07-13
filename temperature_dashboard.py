import tkinter as tk
from tkinter import scrolledtext
import paho.mqtt.client as mqtt
import threading
import hmac
import hashlib
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import datetime

# MQTT Config
BROKER = "localhost"
PORT = 8883
TOPIC = "secure/topic"
USERNAME = "subin"
PASSWORD = "subin123"
CA_CERT = "broker_config/ca.crt"
KEY_FILE = "C:/Users/subin/OneDrive/Desktop(1)/MQTT_Security_Project/shared_key.txt"

with open(KEY_FILE, "r") as f:
    SHARED_KEY = f.read().strip().encode()

# Global Data
temperature_data = []
timestamps = []
labels = []
logs = []
client = None
connected_once = False

# HMAC Verification
def verify_hmac(message, received_hmac):
    calc_hmac = hmac.new(SHARED_KEY, message.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(calc_hmac, received_hmac), calc_hmac

def extract_temperature(message):
    match = re.search(r"Temperature is ([0-9]+)", message)
    return int(match.group(1)) if match else None

def on_connect(client, userdata, flags, rc):
    global connected_once
    if rc == 0 and not connected_once:
        log("✅ Connected to broker securely!")
        client.subscribe(TOPIC)
        connected_once = True
    elif rc != 0:
        log(f"❌ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    if "||" in payload:
        message, received_hmac = payload.split("||", 1)
        valid, expected_hmac = verify_hmac(message, received_hmac)
        log_msg = f"""============================================================
🕒 Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📨 Raw message received: {payload}
🧾 Parsed message: {message}
🔐 HMAC from message: {received_hmac}
""" + (
            "✅ Message is authentic!"
            if valid else f"❌ HMAC verification failed!\n🧮 Expected HMAC: {expected_hmac}"
        ) + "\n============================================================"

        log(log_msg)

        if valid:
            temp = extract_temperature(message)
            if temp is not None:
                temperature_data.append(temp)
                now = datetime.datetime.now()
                timestamps.append(now)
                labels.append(f"{now.strftime('%H:%M:%S')} - Temperature is {temp}°C")
    else:
        log("⚠️ Malformed message received!")

def mqtt_thread():
    global client
    client = mqtt.Client(client_id="dashclient", protocol=mqtt.MQTTv311)
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(ca_certs=CA_CERT)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

# UI Logging
def log(message):
    logs.append(message)
    if len(logs) > 10:
        logs.pop(0)
    log_text.configure(state='normal')
    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, "\n\n".join(logs))
    log_text.configure(state='disabled')
    log_text.yview(tk.END)

def start_listener():
    threading.Thread(target=mqtt_thread, daemon=True).start()
    log("▶️ Listening started...")

# Chart Animator
def animate(i):
    if len(timestamps) > 0:
        ax.clear()
        ax.set_facecolor('#2e2e2e')
        fig.patch.set_facecolor('#2e2e2e')

        # Plot and fill
        ax.plot(timestamps, temperature_data, marker='o', color='cyan', linewidth=2)
        ax.fill_between(timestamps, temperature_data, color='teal', alpha=0.4)

        # Labels above points
        for i, (x, y) in enumerate(zip(timestamps, temperature_data)):
            ax.text(x, y + 2, labels[i], ha='center', fontsize=9, color='white', backgroundcolor='#333333')

        # Aesthetic updates
        ax.set_xlabel("Time", color='white', labelpad=10)
        ax.set_ylabel("Temperature (°C)", color='white', labelpad=10)
        ax.tick_params(colors='white')

        # Format x-axis with datetime
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        fig.autofmt_xdate(rotation=45)
        ax.grid(True, color='#444444')

        # Tight layout
        fig.tight_layout()


# Tkinter Setup
root = tk.Tk()
root.title("MQTT Dashboard")
root.geometry("1200x700")

fig, ax = plt.subplots()
fig.patch.set_facecolor('#2e2e2e')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

control_frame = tk.Frame(root, bg="#2e2e2e")
control_frame.pack(fill=tk.X, side=tk.BOTTOM)

start_btn = tk.Button(control_frame, text="Start Listener", command=start_listener,
                      bg="#4CAF50", fg="white", padx=20, pady=5)
start_btn.pack(side=tk.RIGHT, padx=20, pady=10)

log_text = scrolledtext.ScrolledText(control_frame, height=12, wrap=tk.WORD,
                                      state='disabled', bg="#1e1e1e", fg="lime",
                                      font=("Consolas", 15))
log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

ani = animation.FuncAnimation(fig, animate, interval=2000)

root.mainloop()
