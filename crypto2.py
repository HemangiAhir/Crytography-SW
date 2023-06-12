import time
import win32com.client
import tkinter as tk
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Encrypt the message with a time lock
def encrypt_with_time_lock(message, deadline):
    current_time = time.time()
    if current_time > deadline:
        time_left = deadline
        print("Encryption will expire in", time_left, "seconds.")
        time.sleep(time_left)
    else:
        time_left = deadline - current_time
        time.sleep(time_left)
    cipher = PKCS1_OAEP.new(key.publickey())
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Decrypt the message
def decrypt_message(ciphertext):
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message.decode()

# Example usage
message = input("Enter the message to be encrypted: ")
deadline_str = input("Enter the decryption time (in seconds from now): ")
deadline = time.time() + int(deadline_str)
print(time.time())

encrypted = encrypt_with_time_lock(message, deadline)
print("Message encrypted:", encrypted)

# Simulate waiting until after the deadline
#time.sleep(deadline - time.time())

decrypted = decrypt_message(encrypted)
print("Message decrypted:", decrypted)


outlook = win32com.client.Dispatch("Outlook.Application")

# Get the default Inbox folder
inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)  # 6 represents the Inbox folder

# Create a GUI window using tkinter
window = tk.Tk()
window.title("Outlook Inbox")
window.geometry("500x300")

# Create a listbox to display email subjects
listbox = tk.Listbox(window)
listbox.pack(fill=tk.BOTH, expand=True)

# Loop through the emails in the Inbox folder and add the subjects to the listbox
for mail in inbox.Items:
    listbox.insert(tk.END, mail.Subject)

# Start the GUI event loop
window.mainloop()

