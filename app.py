# app.py
from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import os
import datetime
from io import BytesIO
from urllib.parse import unquote
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or get_random_bytes(24).hex()

# Folders
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
LOG_FOLDER = os.path.join(os.path.dirname(__file__), 'logs')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log intrusion attempts
def log_attempt(ip, user, action, status):
    log_path = os.path.join(LOG_FOLDER, 'intrusion_log.txt')
    with open(log_path, 'a') as f:
        f.write(f"{datetime.datetime.now()} | {ip} | {user} | {action} | {status}\n")

# Hash using SHA-256 (replacing MD5)
def get_hash(data):
    return hashlib.sha256(data).hexdigest()

# Encrypt file with salt + nonce + ciphertext
def encrypt_file(data, password):
    salt = get_random_bytes(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 500000, dklen=32)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return salt + cipher.nonce + ciphertext

# Decrypt file
def decrypt_file(data, password):
    if len(data) < 48:
        raise ValueError("Ciphertext too short")
    salt = data[:32]
    nonce = data[32:48]
    ciphertext = data[48:]
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 500000, dklen=32)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext)

@app.route('/')
def home():
    try:
        files = [f for f in os.listdir(UPLOAD_FOLDER) if f.startswith('enc_')]
    except Exception as e:
        logger.error(f"Error reading upload folder: {e}")
        files = []
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    ip = request.remote_addr
    username = request.form.get('username', 'unknown')

    if 'file' not in request.files:
        flash("❌ No file part in request!")
        log_attempt(ip, username, 'upload', 'FAILED')
        return redirect(url_for('home'))

    file = request.files['file']
    if file.filename == '':
        flash("❌ No file selected!")
        log_attempt(ip, username, 'upload', 'FAILED')
        return redirect(url_for('home'))

    password = request.form['password']
    if len(password) < 4:
        flash("❌ Password must be at least 4 characters!")
        log_attempt(ip, username, 'upload', 'FAILED')
        return redirect(url_for('home'))

    # Secure and unique filename
    original_filename = secure_filename(file.filename)
    unique_suffix = f"{get_random_bytes(8).hex()}"
    enc_filename = f"enc_{unique_suffix}_{original_filename}"
    file_path = os.path.join(UPLOAD_FOLDER, enc_filename)

    try:
        data = file.read()
        if len(data) == 0:
            flash("❌ Cannot upload empty file!")
            return redirect(url_for('home'))

        # Encrypt
        encrypted_data = encrypt_file(data, password)

        # Save encrypted file
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)

        # Save SHA-256 hash
        hash_value = get_hash(data)
        hash_path = file_path + ".sha256"
        with open(hash_path, 'w') as f:
            f.write(hash_value)

        flash(f"✅ '{original_filename}' encrypted and saved securely!")
        logger.info(f"Uploaded and encrypted: {enc_filename}")
        log_attempt(ip, username, 'upload', 'SUCCESS')
        return redirect(url_for('home'))

    except Exception as e:
        logger.error(f"Upload failed: {e}")
        flash("❌ An error occurred during encryption.")
        log_attempt(ip, username, 'upload', 'FAILED')
        return redirect(url_for('home'))

@app.route('/decrypt/<path:filename>')
def decrypt_form(filename):
    # Prevent path traversal
    if '..' in filename or filename.startswith('/'):
        flash("❌ Invalid file path.")
        return redirect(url_for('home'))
    safe_filename = unquote(filename)
    return render_template('decrypt.html', filename=safe_filename)

@app.route('/decrypt_file/<path:filename>', methods=['POST'])
def decrypt_file_route(filename):
    ip = request.remote_addr
    if '..' in filename or filename.startswith('/'):
        flash("❌ Invalid file path.")
        return redirect(url_for('home'))

    password = request.form['password']
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        flash("❌ File not found!")
        log_attempt(ip, 'unknown', 'decrypt', 'FAILED')
        return redirect(url_for('home'))

    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = decrypt_file(encrypted_data, password)

        # Verify integrity
        hash_path = file_path + ".sha256"
        if os.path.exists(hash_path):
            with open(hash_path, 'r') as f:
                original_hash = f.read().strip()
            current_hash = get_hash(decrypted_data)
            if current_hash != original_hash:
                flash("⚠️ Warning: File may have been tampered with!")

        # Extract original filename
        # Format: enc_<uuid>_<original_name>
        original_name = "_".join(filename.split("_")[3:]) if filename.count("_") >= 3 else filename.replace("enc_", "")

        return send_file(
            BytesIO(decrypted_data),
            as_attachment=True,
            download_name=original_name,
            mimetype='application/octet-stream'
        )

    except Exception as e:
        logger.warning(f"Decryption failed for {filename}: {str(e)}")
        flash("❌ Decryption failed! Wrong password or corrupted file.")
        log_attempt(ip, 'unknown', 'decrypt', 'FAILED')
        return redirect(url_for('home'))

# Start the app
if __name__ == '__main__':
    print(f"📁 Uploads: {UPLOAD_FOLDER}")
    print(f"📄 Logs: {LOG_FOLDER}")
    print("🚀 SecureVault is running at http://127.0.0.1:5000")
    app.run(debug=False)  # Set to True only during development