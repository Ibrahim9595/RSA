# Handle converting string to an int
# @params msg: string
# @return int_msg: int
def msg_to_int(msg):
    int_msg = ""
    for ch in msg:
        pre = "{0:b}".format(ord(ch))
        if len(pre) < 7:
            pre = "0" * (7-len(pre)) + pre
        int_msg += pre
    
    return int(int_msg, 2)


# Handle converting int to a string
# @params i: int
# @return msg: string
def int_to_msg(i):
    bin_format = "{0:7b}".format(i)
    msg = ""
    
    for b in range(0, len(bin_format), 7):
        msg += chr(int(bin_format[b:b+7], 2))
    
    return msg