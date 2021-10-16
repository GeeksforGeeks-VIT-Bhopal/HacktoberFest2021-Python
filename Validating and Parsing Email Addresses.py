import re

N = int(input())
for _ in range(N):
    tOrg = input().strip()

    e = re.search(r'<(.*)>', tOrg)
    if e == None:
        continue
    t = e.group(1).strip()

    if re.search(r'^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', t) != None:
        print(tOrg)