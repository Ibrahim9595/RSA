from time import time
from actions import setup, do_encryption, do_decryption
from helpers import msg_to_int, int_to_msg
from tkinter import *

# Handle encryption Action
# @params msg: string, e: int, n: int
# @return encrypted_msg: string
def encryption(msg, e, n):
    int_msg = msg_to_int(msg)
    encrypted = do_encryption(int_msg, e, n)
    # print(setuptime + '\n Encrypted Message = ', encrypted)
    return encrypted

# Handle decryption Action
# @params msg: string, d: int, p: int, q: int
# @return decrypted_msg: string
def decryption(msg, d, p, q):
    decrypted = do_decryption(int(msg), d, p, q)
    # print('\nMessage = ', int_to_msg(decrypted))
    return int_to_msg(decrypted)


s = time() # time start 
RSAparams = setup(512) # initializing the RSA algorithm
s = time() - s # time end

# UI Start
root = Tk()

# Frames
actions_frame = Frame(root)
input_frame = Frame(root)
output_frame = Frame(root)

# Input Section
input_label = Label(input_frame, text="Input: ")
input_msg = Text(input_frame, height=4, width=128)


# Output Section
output_label = Label(output_frame, text="Output: ")
output_msg = Text(output_frame, height=4, width=128)

# Action Section
encrypt = Button(actions_frame, text="Encrypt", command=lambda: output_msg.insert("0.0",encryption(
    input_msg.get("0.0", "128.4").strip(), RSAparams['e'], RSAparams['n'])))
decrypt = Button(actions_frame, text="Decrypt", command=lambda: output_msg.insert("0.0", (decryption(
    input_msg.get("0.0", "128.4").strip(), RSAparams['d'], RSAparams['p'], RSAparams['q']))))

# Setup Time
setup = Label(root, text=("Setup Time = " + str(s) + " sec"))

# Put the different sections in there frames(containers)
# Input
input_label.pack(side=LEFT)
input_msg.pack(side=LEFT)

# Actions
encrypt.pack(side=LEFT)
decrypt.pack(side=LEFT)

# Output
output_label.pack(side=LEFT)
output_msg.pack(side=LEFT)

# Put containers on the screen
input_frame.pack()
actions_frame.pack()
output_frame.pack()
setup.pack()

root.mainloop()
