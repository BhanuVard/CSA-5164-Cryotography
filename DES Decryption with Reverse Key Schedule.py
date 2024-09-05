from pyDes import des, CBC, PAD_PKCS5

def des_decrypt(ciphertext, key):
    des_obj = des(key, CBC)
    return des_obj.decrypt(ciphertext)

# Example usage
ciphertext = b'your encrypted text'
key = b'12345678'  # DES uses a 56-bit key (8-byte in this example)
decrypted_text = des_decrypt(ciphertext, key)
print(decrypted_text)
