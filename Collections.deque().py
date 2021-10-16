from collections import deque
d = deque()
for i in range(int(input())):
    s = input().split()
    if s[0] == 'append':
        d.append(s[1])
    elif s[0] == 'appendleft':
        d.appendleft(s[1])
    elif s[0] == 'pop':
        d.pop()
    else:
        d.popleft()
print( " ".join(d))
