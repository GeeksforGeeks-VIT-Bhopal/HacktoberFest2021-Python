K = int(input())
set_S = set()
sumlist_S = 0
for i in input().split():
    I = int(i)
    set_S.add(I)
    sumlist_S += I

print((sum(set_S)*K - sumlist_S)//(K-1))