# 🧠 Python Keylogger Simulation (Educational Use Only)

This project is a **Python-based keylogger simulation**, created for **educational and ethical hacking practice**. It demonstrates how keystrokes can be captured, encrypted securely, and sent over a network socket to a remote server. A companion server script is included to decrypt and display the captured data in real-time.

> ⚠️ **Disclaimer**: This tool is strictly for learning and testing in authorized environments. Do not use this code on any system you do not own or have explicit permission to test. Unauthorized use is illegal and unethical.

---
## 📂 Project Structure

```
📁 keylogger_project/
├── snatcher.py        # Keylogger
├── snatch-server.py   # Server to receive exfiltrated data 
└── README.md          # Project documentation
```

## 🚀 Features

- ⌨️ Captures keystrokes (including special keys like `<enter>`, `<space>`, `<ctrl>`, etc.)
- 🔐 Encrypts keystroke logs using **Fernet** with a **PBKDF2-HMAC-SHA256** derived key
- 📡 Sends encrypted logs via TCP socket to a remote server
- 🔓 Includes server-side script to decrypt and print the logs
- 🧪 Useful for simulating malware behavior and learning secure data handling

---

## 📦 Requirements

Install required packages:

```bash
pip install pynput cryptography
````

---

## 🛠️ Usage

### 1. Run the Server (Receiver)

Start the server to accept and decrypt incoming keylog data:

```bash
python3 snatch-server.py
```

### 2. Run the Keylogger (Victim)

Update the `HOST` in `keylogger.py` to the IP address of your server machine:

```python
HOST = "YOUR_SERVER_IP"
PORT = 12345
```

Then run the keylogger (in background):

```bash
python3 snatcher.py &
```

The script will:

* Capture typed keystrokes
* Wait for `Enter` to send the batch
* Encrypt the input
* Send it over the network to the receiver

---

## 🔄 How Encryption Works

* A **random salt** is generated for each message
* A key is derived from the password using **PBKDF2-HMAC-SHA256** (1.2M iterations)
* The derived key is encoded into a Fernet key
* The message is encrypted using **Fernet**
* The final payload is `salt + ciphertext`, base64-encoded and sent via TCP

---

## 💡 Educational Value

This project is useful for:

* Understanding how keyloggers operate
* Learning about Fernet and PBKDF2 encryption in Python
* Practicing socket programming
* Simulating real-world malware behavior for red team education
* Raising awareness of endpoint security threats

---

## 🧑‍⚖️ License & Ethics

This code is released for **responsible educational use only**.
Do **not** use this in real-world scenarios or against any unauthorized targets.

---

## 👤 Author

**Pevinkumar A**
Cybersecurity Learner | Python Developer | Ethical Hacker in Training

