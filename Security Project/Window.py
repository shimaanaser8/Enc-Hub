import string
import tkinter as tk
from tkinter import ttk
from AES import bytes_to_string, decrypt_aes, encrypt_aes, string_to_bytes
from DES import DES_encryption , DES_decryption
from Vigenere import encrypt_vigenere_cipher , decrypt_vigenere_cipher
from Playfair import encrypt_playfair_cipher , decrypt_playfair_cipher


def encrypt_decrypt():
    method = method_var.get()
    action = action_var.get()
    plaintext = plaintext_entry.get()
    key = key_entry.get()  
    result = ""
    
    # Perform encryption or decryption based on the selected method and action
    if method == "Transposition Row":
        if action == "Encryption":
            
            result = (plaintext, key)
            
        elif action == "Decryption":
            
            result = (plaintext, key)
            
    elif method == "Caesar":
        if action == "Encryption":
            
            result = (plaintext, key)
            
        elif action == "Decryption":
            
            result = (plaintext, key)
            
    elif method == "Vigenere":
        if action == "Encryption":
            
            result = encrypt_vigenere_cipher(plaintext, key)
            
        elif action == "Decryption":
           
            result = decrypt_vigenere_cipher(plaintext, key)
            
    elif method == "Playfair":
        if action == "Encryption":
            result = encrypt_playfair_cipher(key , plaintext)
            
        elif action == "Decryption":
            
            result = decrypt_playfair_cipher(plaintext, key)
            
    elif method == "DES":
        if action == "Encryption":
            result = DES_encryption(plaintext , key)
            
        elif action == "Decryption":
            
            result = DES_decryption(plaintext, key)
        
    elif method == "AES":
        if action == "Encryption":
            plaintext = string_to_bytes(plaintext)
            key = string_to_bytes(key)
            ciphertext = encrypt_aes(plaintext, key)
            c=bytes_to_string(ciphertext)
            result = c
            
        elif action == "Decryption":
            plaintext = string_to_bytes(plaintext)
            key = string_to_bytes(key)
            decrypted_message = decrypt_aes(plaintext, key)
            d=bytes_to_string(decrypted_message)
            result = d
            
    elif method == "Railfence":
        if action == "Encryption":
    
            result = (plaintext, key)
            
        elif action == "Decryption":
            
            result = (plaintext, key)
            
    elif method == "Polyalphabetic":
        if action == "Encryption":
    
            result = (plaintext, key)
            
        elif action == "Decryption":
            
            result = (plaintext, key)
            
    elif method == "Monoalphabetic":
        if action == "Encryption":
    
            result = (plaintext, key)
            
        elif action == "Decryption":
            
            result = (plaintext, key)
    
    result_label.config(text="Result: " + result)

# Create main window
window = tk.Tk()
window.title("Encryption/Decryption Tool")

# Create frame for left side elements
left_frame = ttk.Frame(window)
left_frame.pack(side="left", padx=20, pady=20)

# Encryption/Decryption Method dropdown
method_label = ttk.Label(left_frame, text="Choose Method:")
method_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
method_var = tk.StringVar()
method_dropdown = ttk.Combobox(left_frame, textvariable=method_var, values=["Transposition Row", "Caesar", "DES", "AES", "Polyalphabetic", "Monoalphabetic", "Railfence", "Playfair", "Vigenere"])
method_dropdown.grid(row=0, column=1, padx=5, pady=5)
method_dropdown.current(0)

# Encryption/Decryption Action radiobuttons
action_label = ttk.Label(left_frame, text="Choose Action:")
action_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
action_var = tk.StringVar(value="Encryption")
encrypt_radio = ttk.Radiobutton(left_frame, text="Encryption", variable=action_var, value="Encryption")
encrypt_radio.grid(row=1, column=1, padx=5, pady=5, sticky="w")
decrypt_radio = ttk.Radiobutton(left_frame, text="Decryption", variable=action_var, value="Decryption")
decrypt_radio.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Plain/Cipher Text entry
plaintext_label = ttk.Label(left_frame, text="Enter Plain/Cipher Text:")
plaintext_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
plaintext_entry = ttk.Entry(left_frame, width=30)
plaintext_entry.grid(row=3, column=1, padx=5, pady=5)

# Key entry
key_label = ttk.Label(left_frame, text="Enter Key:")
key_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
key_entry = ttk.Entry(left_frame, width=30)
key_entry.grid(row=4, column=1, padx=5, pady=5)

# Encrypt/Decrypt button
encrypt_decrypt_button = ttk.Button(left_frame, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_decrypt_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Result label
result_label = ttk.Label(left_frame, text="Result: ")
result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()