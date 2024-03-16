import tkinter as tk
from tkinter import messagebox

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

# Reverse dictionary for decoding
reverse_morse_dict = {v: k for k, v in morse_code_dict.items()}

def encrypt_message(event=None):
    message = entry_text.get("1.0", "end-1c")
    if not message.strip():
        messagebox.showerror("Error", "Please enter a message to encrypt.")
        return
    morse_code = encrypt_to_morse(message)
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", morse_code)
    output_text.config(state="disabled")

def decrypt_message(event=None):
    morse_code = entry_text.get("1.0", "end-1c")
    if not morse_code.strip():
        messagebox.showerror("Error", "Please enter Morse code to decrypt.")
        return
    message = decrypt_from_morse(morse_code)
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", message)
    output_text.config(state="disabled")

def encrypt_to_morse(text):
    encoded = []
    for char in text.upper():
        if char in morse_code_dict:
            encoded.append(morse_code_dict[char])
    return ' '.join(encoded)

def decrypt_from_morse(morse_code):
    decoded = []
    for code in morse_code.split():
        if code in reverse_morse_dict:
            decoded.append(reverse_morse_dict[code])
    return ''.join(decoded)

# Create the main window
root = tk.Tk()
root.title("Morse Code Encryptor & Decryptor")

# Create frame for input field and buttons
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Input field for text
entry_text_label = tk.Label(input_frame, text="Enter message or Morse code:", font=('Arial', 12))
entry_text_label.grid(row=0, column=0, padx=5, pady=5)
entry_text = tk.Text(input_frame, height=3, width=30, font=('Arial', 18))
entry_text.grid(row=1, column=0, padx=5)

# Buttons for encrypting and decrypting
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt_message, font=('Arial', 12))
encrypt_button.grid(row=0, column=0, padx=5)
decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt_message, font=('Arial', 12))
decrypt_button.grid(row=0, column=1, padx=5)

# Output field for Morse code or decrypted message
output_frame = tk.Frame(root)
output_frame.pack(pady=10)
output_text_label = tk.Label(output_frame, text="Encrypted or Decrypted Message:", font=('Arial', 12))
output_text_label.grid(row=0, column=0, padx=5, pady=5)
output_text = tk.Text(output_frame, height=3, width=30, font=('Arial', 18), state="disabled")
output_text.grid(row=1, column=0, padx=5)

root.mainloop()