# Python Password Manager

A secure desktop password manager built with Python and tkinter for my software development portfolio.

## 🚀 Features

- Generate strong passwords with customizable criteria
- Encrypted local storage (AES-256)
- Clean tkinter GUI
- Master password authentication
- Search and copy passwords
- Secure clipboard management

## 🛠️ Tech Stack

- **Python 3.8+** with tkinter
- **SQLite** for local data
- **cryptography** for AES encryption
- **secrets** for secure password generation

## ⚡ Quick Start

```bash
git clone https://github.com/username/python-password-manager.git
cd python-password-manager
python3 -m venv password-manager-env
source password-manager-env/bin/activate
pip install -r requirements.txt
python main.py
```

## 🎯 Project Goals

This demonstrates:
- Desktop app development with Python
- Security implementation (encryption, hashing)
- Clean architecture patterns
- GUI design with tkinter

## 🔐 Security

- AES-256 encryption for stored passwords
- Salted hashing for master password
- Local-only storage (no network transmission)
- Cryptographically secure password generation

## 📁 Structure

```
password_manager/
├── src/
│   ├── models/     # Data models
│   ├── services/   # Business logic  
│   └── ui/         # GUI components
├── tests/          # Unit tests
└── main.py         # Entry point
```

## 🚧 Roadmap

**Phase 1**: Desktop app (current)  
**Phase 2**: Browser extension integration  
**Phase 3**: Auto-fill capabilities

## 📄 License

MIT License - see `LICENSE` file

---

⭐ **Portfolio Project** - Built to showcase Python development skills