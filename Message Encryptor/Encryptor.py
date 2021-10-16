import rsa

(pubkey, privkey) = rsa.newkeys(512)

def encrypt_msg(msg):
    utf8_msg = msg.encode("utf-8")

    return rsa.encrypt(utf8_msg, pubkey)


def decrypt_msg(crypto):
    uft8_msg = rsa.decrypt(crypto, privkey)
    msg = uft8_msg.decode("utf-8")

    return msg

