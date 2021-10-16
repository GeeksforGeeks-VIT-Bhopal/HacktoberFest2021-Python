n,m=list(map(int, input().split()))
ns=list(map(int, input().split()))
h=set(map(int, input().split()))
s=set(map(int, input().split()))
res=0

for x in ns:
    if x in h:
        res+=1
    elif x in s:
        res-=1
print(res)