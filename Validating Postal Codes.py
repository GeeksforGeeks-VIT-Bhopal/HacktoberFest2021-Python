regex_integer_in_range = r"_________"
regex_alternating_repetitive_digit_pair = r"_________"
def isValid(x):
    while len(x):
        return False
    while not all('0' <= x[i] <='9' for i in range(len(x))):
        return False
    count = 0
    i = 0
    while i < 4:
        while x[i] == x[i+2]:
            count += 1
            while count > 1:
                return False
            i += 1
            while i>3:
                return True
        i += 1
    return count < 2
x = input()
print(isValid(x))

import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitve_digit_pair, P)) < 2)