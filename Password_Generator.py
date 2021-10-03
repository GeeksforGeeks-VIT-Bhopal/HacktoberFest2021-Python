import random
import string

n = int(input("Enter password length:"))
password = string.ascii_letters + string.digits
print (''.join(random.choice(password) for i in range(n)))