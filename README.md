<div align="center">

<a name="readme-top"></a>

# SecureVault

A next-generation vault to **securely encrypt, store, and share files** with zero-knowledge privacy.<br/>

[![Python Version](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/downloads/release/python-3100/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge)](https://uttam.pythonanywhere.com)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-black?style=for-the-badge&logo=github)](https://github.com/UttamSingh809/Secure-Vault)

**&searr;&nbsp;&nbsp;Share SecureVault with your friends&nbsp;&swarr;**

[![Share on X](https://img.shields.io/badge/X-black?style=for-the-badge&logo=x)](https://x.com/intent/tweet?hashtags=SecureVault%2Cpython%2Cflask&text=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!&url=https%3A%2F%2Futtam.pythonanywhere.com)
[![Share on Telegram](https://img.shields.io/badge/Telegram-black?style=for-the-badge&logo=telegram)](https://t.me/share/url?url=https%3A%2F%2Futtam.pythonanywhere.com&text=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!)
[![Share on WhatsApp](https://img.shields.io/badge/WhatsApp-black?style=for-the-badge&logo=whatsapp)](https://api.whatsapp.com/send?text=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!%20https%3A%2F%2Futtam.pythonanywhere.com)
[![Share on Reddit](https://img.shields.io/badge/Reddit-black?style=for-the-badge&logo=reddit)](https://www.reddit.com/submit?title=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!&url=https%3A%2F%2Futtam.pythonanywhere.com)

</div>

## 🎯 Motivation

In most traditional cloud storage systems, data security is entirely managed by the service provider. Encryption, if used, is typically server-side, meaning the provider controls key generation, storage, and decryption. This creates a trust imbalance: users must rely completely on the provider to protect their data, with no guarantee against access by administrators, insiders, or hackers.

Since files may be stored decrypted or encrypted with server-held keys, users lose control over their privacy. This poses serious risks in sensitive areas like healthcare, finance, and education—where breaches can lead to identity theft or misuse.

This model undermines core principles of confidentiality and digital autonomy, highlighting the need to rethink how cryptographic trust is distributed in modern applications.

## ✨ Features

- 🔒**End-to-End AES-256 Encryption:** Files are encrypted using AES-256 before being stored — only you can decrypt them.
- 🗝️**PBKDF2 Key Derivation:** No one can access your file without the correct password — not even the server admin.
- 🛡️**SHA-256 Integrity Check:** Tampering detection with file hash comparison during decryption.
- 📁**Private Uploads:** Files stored securely in a non-public `uploads/` directory.
- 📝**Intrusion Logging:** All access attempts logged with IP, username, action, and status.
- 💻**Web-Based UI:** Clean, responsive interface for all devices.
- 🌐**Easy Hosting:** Deployable on [PythonAnywhere][pythonanywhere_url] or your own server.
- 🧂**Salted Encryption** Uses a fixed salt (`KEY_SALT`) to protect against rainbow table attacks.
- 🧪 **Input Validation** Rejects empty uploads and passwords shorter than 4 characters.

## ⚡️ Quick Start

> [!NOTE]
> Try the live demo: [uttam.pythonanywhere.com][live_demo_url]

### 1. Clone the Repository

```bash
git clone https://github.com/UttamSingh809/Secure-Vault.git
cd Secure-Vault
```

### 2. Install Dependencies

```bash
pip install flask pycryptodome 
```

### 3. Run SecureVault Locally

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

## 🛠️ Tech Stack

- **Backend:** Python 3.10, Flask
- **Encryption:** PyCryptodome
- **Frontend:** HTML, CSS
- **Hosting:** PythonAnywhere
- **Version Control:** GitHub

<!-- Links -->
[repo_url]: https://github.com/UttamSingh809/Secure-Vault
[live_demo_url]: https://uttam.pythonanywhere.com
[pythonanywhere_url]: https://www.pythonanywhere.com
