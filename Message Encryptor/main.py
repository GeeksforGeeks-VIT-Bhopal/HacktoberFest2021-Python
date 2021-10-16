from tkinter import *
from Encryptor import decrypt_msg, encrypt_msg

root = Tk()
root.title("Message Encryptor")
root.geometry("900x300")

# input fields
msg = Entry(root)
crypto = Entry(root)

# label fields
crypto_label = Text(root, height=1, borderwidth=0)
msg_label = Text(root, height=1, borderwidth=0)
divider_label = Label(root, text="============================================================================", pady=60)


def change_crypto_label_txt(msg):
    crypto_label.insert(1.0, encrypt_msg(msg.get()))


def change_msg_label_txt(crypto):
    msg_label.insert(1.0, decrypt_msg(crypto.get()))


# button fields
encrypt_btn = Button(root, text="Encrypt", command=lambda: change_crypto_label_txt(msg), padx=100)
decrypt_btn = Button(root, text="Decrypt", command=lambda: change_msg_label_txt(crypto), padx=100)


# adding the widgets into the window
msg.pack()
crypto_label.pack()
encrypt_btn.pack()
divider_label.pack()
crypto.pack()
msg_label.pack()
decrypt_btn.pack()


root.mainloop()