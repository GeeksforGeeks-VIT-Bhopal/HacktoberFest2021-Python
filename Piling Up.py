from collections import deque
def check(d):
    while d:
        big = d.popleft() if d[0]>d[-1] else d.pop()
        if not d:
            return "Yes"
        if d[-1]>big or d[0]>big:
            return "No"
    
for i in range(int(input())):
    int(input())
    d = deque(map(int,input().split()))
    print(check(d))
        