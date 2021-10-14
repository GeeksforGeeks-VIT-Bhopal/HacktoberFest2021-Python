import string
import random

pslen=int(input("Enter your password length"))

LCC = string.ascii_lowercase
UCC = string.ascii_uppercase
Digits = string.digits
Symbols = string.punctuation

Total =  UCC + LCC + Symbols + Digits

temp=random.sample(Total,pslen)
password = "".join(temp)

print(password)
