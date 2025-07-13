# AUTHENTICATION-AND-INTEGRITY-FOR-MQTT-PROTOCOL
🛡️ MQTT Security Project Secure MQTT with:  🔐 TLS encryption  🔑 Client authentication  🧾 HMAC message integrity  Includes:  🐍 Python pub/sub scripts  🛠️ Certificate generation tools  📊 Flask dashboard for live data  Built with Mosquitto, focused on secure IoT communication.

# 🛡️ MQTT Security Project

A secure MQTT communication system using **Mosquitto** with **TLS encryption**, **client certificate authentication**, and **HMAC integrity protection**. Built for secure, lightweight, real-time messaging in embedded and IoT environments.

> 🎓 This project was developed as part of the **Embedded Security** course in the **Master’s in Applied Computer Science** program at **Deggendorf Institute of Technology (DIT), Germany**.

---

## 🔧 Features

- 🔐 **TLS Encryption** — Secures MQTT communication
- 🔑 **Mutual Authentication** — Server and clients authenticate via X.509 certificates
- 🧾 **HMAC (SHA-256)** — Ensures message integrity and authenticity
- 🐍 **Python MQTT Clients** — Secure publisher and subscriber scripts
- 📊 **Flask Dashboard (Optional)** — Real-time data visualization via MQTT
- 🛠️ **Certificate Generation Scripts** — Simplifies CA and key creation

---

## 📁 Project Structure

```
MQTT_Security_Project/
├── certs/                 # TLS certificates & CA scripts
│   ├── generate_ca.sh
│   ├── generate_server_cert.sh
│   └── generate_client_cert.sh
│
├── mqtt_clients/          # Secure Python pub/sub scripts
│   ├── publisher.py
│   └── subscriber.py
│
├── broker_config/         # Mosquitto TLS config
│   ├── mosquitto.conf
│   └── passwords.txt
│
├── dashboard/             # Flask MQTT dashboard (optional)
│   ├── app.py
│   ├── templates/
│   └── static/
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/MQTT_Security_Project.git
cd MQTT_Security_Project
```

### 2. Generate Certificates
```bash
cd certs
chmod +x *.sh
./generate_ca.sh
./generate_server_cert.sh
./generate_client_cert.sh
```

### 3. Configure and Start Mosquitto
```bash
mosquitto -c broker_config/mosquitto.conf
```

### 4. Run the MQTT Clients
```bash
# Terminal 1
python3 mqtt_clients/subscriber.py

# Terminal 2
python3 mqtt_clients/publisher.py
```

### 5. Launch the Optional Dashboard
```bash
cd dashboard
pip install -r requirements.txt
python3 app.py
```

---

## 📌 Requirements

- Python 3.6+
- Mosquitto (with TLS support)
- OpenSSL
- Flask (for dashboard)

---

## 🔒 Security Overview

| Component           | Method            |
|--------------------|-------------------|
| Encryption         | TLS 1.2 / 1.3     |
| Authentication     | X.509 Certificates|
| Message Integrity  | HMAC-SHA256       |

---

## 📷 Screenshots *(Optional)*

_Add dashboard or terminal output screenshots here if available._

---

## 📚 Academic Context

This repository is part of a university project submitted to:  
**Course:** Embedded Security  
**Program:** M.Sc. Applied Computer Science  
**Institution:** Deggendorf Institute of Technology, Germany  
**Year:** 2025  

---

## 📃 License & Rights

© 2025 **Subin Samu**. All rights reserved.  
This project is provided for educational and non-commercial purposes only. Unauthorized reproduction or redistribution is prohibited.

---

## 💬 Final Thought

> *"Everything in this world can be taken away from you, except the knowledge you have gained. One thing that won’t leave you is knowledge. So, learn, learn, learn anything. Once you start gaining the power of knowledge, you won’t step back."*  
> — **Subin Samu**

---
