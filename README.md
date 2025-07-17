# AUTHENTICATION-AND-INTEGRITY-FOR-MQTT-PROTOCOL
🛡️ MQTT Security Project Secure MQTT with:  🔐 TLS encryption  🔑 Client authentication  🧾 HMAC message integrity  Includes:  🐍 Python pub/sub scripts  🛠️ Certificate generation tools  📊 Flask dashboard for live data  Built with Mosquitto, focused on secure IoT communication.

<div align="center">

# 🛡️ MQTT Security Project  
**Secure, Authenticated, and Verified Communication for IoT Systems**

🚀 Developed for the **Embedded Security** course at  
🎓 **Deggendorf Institute of Technology (DIT), Germany**  
📅 **Year:** 2025  
👨‍💻 **Author:** Subin Samu

</div>

---

## ✨ Overview

This project implements a **secure MQTT communication system** using:

- 🔐 **TLS encryption**
- 🔑 **Client certificate-based authentication**
- 🧾 **HMAC (SHA-256) for integrity**

Designed to protect MQTT messaging for IoT/embedded systems from eavesdropping, spoofing, and tampering.

---

## 🔧 Features

| Feature                     | Description                                           |
|----------------------------|-------------------------------------------------------|
| ✅ TLS Encryption           | Encrypts MQTT messages in transit                     |
| ✅ Mutual Authentication    | Both client and broker verify identity via X.509     |
| ✅ HMAC Integrity Check     | Detects any message tampering                        |
| ✅ Python Pub/Sub Scripts   | Secured publisher and subscriber examples            |
| ✅ Flask Dashboard (Optional)| Real-time MQTT message visualizer                    |
| ✅ Easy Certificate Setup   | Auto scripts to create CA and client/server certs    |

---

## 📁 Project Structure

```
MQTT_Security_Project/
├── certs/                 → Certificate generation scripts
├── mqtt_clients/          → Secure Python publisher & subscriber
├── broker_config/         → Mosquitto TLS configuration
├── dashboard/             → Flask-based live dashboard (optional)
└── README.md              → You're here!
```

---

## 🚀 Quick Start

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/your-username/MQTT_Security_Project.git
cd MQTT_Security_Project
```

### 🔹 2. Generate Certificates
```bash
cd certs
chmod +x *.sh
./generate_ca.sh
./generate_server_cert.sh
./generate_client_cert.sh
```

### 🔹 3. Start Mosquitto Broker
```bash
mosquitto -c broker_config/mosquitto.conf
```

### 🔹 4. Run MQTT Clients
```bash
# Terminal 1
python3 mqtt_clients/subscriber.py

# Terminal 2
python3 mqtt_clients/publisher.py
```

### 🔹 5. Start Dashboard (Optional)
```bash
cd dashboard
pip install -r requirements.txt
python3 app.py
```

---

## ⚙️ Requirements

- Python 3.6+
- Eclipse Mosquitto (with TLS support)
- OpenSSL
- Flask (for web dashboard)

---

## 🔒 Security Overview

| Security Layer     | Mechanism             |
|--------------------|------------------------|
| Encryption         | TLS 1.2 / 1.3          |
| Authentication     | X.509 Certificates     |
| Message Integrity  | HMAC-SHA256            |

---

## 📚 Academic Context

> **Course:** Embedded Security  
> **Program:** M.Sc. Applied Computer Science  
> **University:** Deggendorf Institute of Technology, Germany  
> **Submitted By:** Subin Samu  
> **Year:** 2025

---

## 📃 License & Rights

© 2025 **Subin Samu**. All rights reserved.  
This project is intended for academic and non-commercial use only. Unauthorized reproduction or redistribution is prohibited.

---

## 💬 Final Thought

> 🧠 *"Everything in this world can be taken away from you, except the knowledge you have gained. One thing that won’t leave you is knowledge. So, learn, learn, learn anything. Once you start gaining the power of knowledge, you won’t step back."*  
> — **Subin Samu**

---

