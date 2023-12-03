from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet cipher object
cipher_suite = Fernet(key)

# Encrypt a message
message = b"Hello, this is a secret message."
cipher_text = cipher_suite.encrypt(message)
print("Encrypted:", cipher_text)

# Decrypt the message
decrypted_message = cipher_suite.decrypt(cipher_text)
print("Decrypted:", decrypted_message.decode())
