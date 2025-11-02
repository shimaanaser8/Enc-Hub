def encrypt_vigenere_cipher(plaintext , key):
    key = key.lower()
    plaintext = plaintext.lower()
    key = [ord(char) - ord('a') for char in key]
    ciphertext = [chr((ord(p) - ord('a') + key[i % len(key)]) % 26 + ord('a')) if p.isalpha() else p for i, p in enumerate(plaintext)]
    return ''.join(ciphertext)

def decrypt_vigenere_cipher(ciphertext , key):
    key = key.lower()
    ciphertext = ciphertext.lower()
    key = [ord(char) - ord('a') for char in key]
    plaintext = [chr((ord(c) - ord('a') - key[i % len(key)]) % 26 + ord('a')) if c.isalpha() else c for i, c in enumerate(ciphertext)]
    return ''.join(plaintext)