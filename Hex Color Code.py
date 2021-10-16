import re

N=int(input())

for i in range(0,N):
    s=input()
    x=s.split()

    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        [print(i) for  i in x]