from cryptography.fernet import Fernet

def generate_key():
    """Gera E Salva Uma Nova Chave De Criptografia"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key Generated And Saved As 'secret.key'")

def load_key():
    """Carrega A Chave De Criptografia"""
    return open("secret.key", "rb").read()

def encrypt_link(link):
    """Criptografa O Link E O Salva Em 'video_link.txt'"""
    key = load_key()
    cipher_suite = Fernet(key)
    encrypted_link = cipher_suite.encrypt(link.encode())
    with open("video_link.txt", "wb") as file:
        file.write(encrypted_link)
    print("Link Encrypted And Saved To 'video_link.txt'")

def decrypt_link():
    """Descriptografa O Link Armazenado Em 'video_link.txt'"""
    key = load_key()
    cipher_suite = Fernet(key)
    with open("video_link.txt", "rb") as file:
        encrypted_link = file.read()
    decrypted_link = cipher_suite.decrypt(encrypted_link).decode()
    return decrypted_link
