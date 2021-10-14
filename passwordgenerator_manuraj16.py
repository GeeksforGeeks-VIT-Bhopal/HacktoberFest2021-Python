#Random password generator

import string
import random

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

len = int(input("Enter hte legnth of password "))

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)
print ("Your password is :")
print ("".join(s[:len]))
