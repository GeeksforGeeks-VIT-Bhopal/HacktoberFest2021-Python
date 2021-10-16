from collections import defaultdict

d = defaultdict(list)
list1=[]
n, m = map(int,input().split())

for i in range(1, n+1):
    d[input()].append(str(i))

for i in range(m):
    b = input()
    if b in d: print(' '.join(d[b]))
    else: print(-1)