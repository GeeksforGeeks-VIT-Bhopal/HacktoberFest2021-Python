import re

for i in range(int(input())):
    uid = input()
    if re.search(r'^[a-zA-Z0-9]{10}$',uid):
        flag = 1
        for r in range(10):
            if uid.count(uid[r]) == 1:
                continue
            else:
                flag = 0
                break
        if len(re.findall(r'[A-Z]',uid)) >= 2 and len(re.findall(r'[0-9]',uid)) >= 3 and flag:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')