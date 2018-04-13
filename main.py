from time import time
from actions import setup, do_encryption, do_decryption
from helpers import msg_to_int, int_to_msg
from tkinter import *

def encryption(msg, e, n):
    int_msg = msg_to_int(msg)
    encrypted = do_encryption(int_msg, e, n)
    print(setuptime + '\n Encrypted Message = ', encrypted)
    return encrypted

def decryption(msg, d, p, q):
    decrypted = do_decryption(int(msg), d, p, q)
    print('\nMessage = ', int_to_msg(decrypted))
    return int_to_msg(decrypted)


s = time()
RSAparams = setup(512)
s = time() - s
root = Tk()
output = StringVar()
msg = Text(root, height=4, width=128)
frame = Frame(root)
encrypt = Button(frame, text="Encrypt", command=lambda: encryption(
    msg.get("0.0", "128.4").strip(), RSAparams['e'], RSAparams['n']))
decrypt = Button(frame, text="Decrypt", command=lambda: output.set('Message = '+decryption(
    msg.get("0.0", "128.4").strip(), RSAparams['d'], RSAparams['p'], RSAparams['q'])))
result = Label(root, textvariable=output)

msg.pack()
encrypt.pack(side=LEFT)
decrypt.pack(side=LEFT)
frame.pack()
result.pack()
setuptime = "Setup Time = " + str(s) + " sec"
output.set(setuptime)

root.mainloop()