import string

shift = 9


def encrypt_msg(msg):

    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)

    return msg.translate(table)


def decrypt_msg(msg):

    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[(26 - shift):] + alphabet[:(26 - shift)]
    table = str.maketrans(alphabet, shifted_alphabet)

    return msg.translate(table)