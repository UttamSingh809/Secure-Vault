<div align="center">

<a name="readme-top"></a>

# SecureVault

A next-generation vault to **securely encrypt, store, and share files** with zero-knowledge privacy.<br/>
Built with ❤️ at [Graphic Era Hill University (GEHU)](https://gehu.ac.in) for **TCS 392 – Web Technologies**.

[![Python Version](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/downloads/release/python-3100/)
[![License](https://img.shields.io/github/license/UttamSingh809/Secure-Vault?style=for-the-badge)](https://github.com/UttamSingh809/Secure-Vault/blob/main/LICENSE)
[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge)](https://uttam.pythonanywhere.com)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-black?style=for-the-badge&logo=github)](https://github.com/UttamSingh809/Secure-Vault)

**&searr;&nbsp;&nbsp;Share SecureVault with your friends&nbsp;&swarr;**

[![Share on X](https://img.shields.io/badge/X-black?style=for-the-badge&logo=x)](https://x.com/intent/tweet?hashtags=SecureVault%2Cpython%2Cflask&text=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!&url=https%3A%2F%2Futtam.pythonanywhere.com)
[![Share on Telegram](https://img.shields.io/badge/Telegram-black?style=for-the-badge&logo=telegram)](https://t.me/share/url?url=https%3A%2F%2Futtam.pythonanywhere.com&text=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!)
[![Share on WhatsApp](https://img.shields.io/badge/WhatsApp-black?style=for-the-badge&logo=whatsapp)](https://api.whatsapp.com/send?text=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!%20https%3A%2F%2Futtam.pythonanywhere.com)
[![Share on Reddit](https://img.shields.io/badge/Reddit-black?style=for-the-badge&logo=reddit)](https://www.reddit.com/submit?title=Check%20out%20SecureVault%20%E2%80%93%20an%20end-to-end%20encrypted%20file%20storage%20solution!&url=https%3A%2F%2Futtam.pythonanywhere.com)

</div>

## ✨ Features

- **End-to-End AES-256 Encryption:** Files encrypted with AES (EAX mode) before storage.
- **PBKDF2 Key Derivation:** Password-based key generation with salt & 500k iterations.
- **SHA-256 Integrity Check:** Tampering detection with file hash comparison during decryption.
- **Private Uploads:** Files stored securely in a non-public `uploads/` directory.
- **Intrusion Logging:** All access attempts logged with IP, username, action, and status.
- **Web-Based UI:** Clean, responsive interface for all devices.
- **Auto-Cleanup Ready:** Designed for future features like auto-delete & file expiry.
- **Easy Hosting:** Deployable on [PythonAnywhere][pythonanywhere_url] or your own server.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

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
pip install -r requirements.txt
```

### 3. Run SecureVault Locally

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 🛠️ Tech Stack

- **Backend:** Python 3.10, Flask
- **Encryption:** PyCryptodome (AES, PBKDF2, SHA-256)
- **Frontend:** HTML, CSS
- **Hosting:** PythonAnywhere
- **Version Control:** GitHub

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 🎯 Motivation

In today’s digital age, our files and personal data are constantly at risk—from accidental leaks, malicious actors, or even unintentional insider threats. Most cloud storage solutions, even those that promise encryption, still require you to trust someone else with your keys or your data. What if you could be absolutely sure that nobody but you could access your files—not even the server owner or developer?

That’s why SecureVault exists.

SecureVault was born from a desire to empower people with real privacy, not just promises. It puts the encryption keys in your hands, ensuring that your data remains completely private, even from the platform itself. Whether you’re a student storing assignments, a professional managing sensitive documents, or just someone who values privacy, SecureVault gives you control.

But it’s not just about cryptography or security jargon—SecureVault is designed for everyone. It combines robust, modern encryption (AES-256, PBKDF2, SHA-256) with a clean, intuitive interface. You don’t need to be a tech expert to use it; you just need to care about your privacy. Every upload is encrypted before it leaves your device, and every download is checked for integrity.

We also believe in transparency and community. That’s why SecureVault is open source, so anyone can verify, improve, and trust the code. Our goal is to make strong security accessible, understandable, and usable for everyone, everywhere.

If you’ve ever worried about who might see your files—or if you just want to take control of your data—SecureVault is for you. Join us on the journey to make privacy a default, not a privilege.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## ❤️ Support the Author

If SecureVault helps you or your organization, consider supporting its development! Every bit goes towards maintaining servers and building new features.

<a href="https://www.buymeacoffee.com/uttamsingh809" target="_blank"><img width="200" alt="Support on BuyMeACoffee" src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"/></a>

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

<!-- Links -->
[repo_url]: https://github.com/UttamSingh809/Secure-Vault
[repo_issues_url]: https://github.com/UttamSingh809/Secure-Vault/issues
[repo_pull_request_url]: https://github.com/UttamSingh809/Secure-Vault/pulls
[repo_discussions_url]: https://github.com/UttamSingh809/Secure-Vault/discussions
[repo_license_url]: https://github.com/UttamSingh809/Secure-Vault/blob/main/LICENSE
[live_demo_url]: https://uttam.pythonanywhere.com
[pythonanywhere_url]: https://www.pythonanywhere.com
