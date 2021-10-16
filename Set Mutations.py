a = int(input())
A = set(map(int, input().split()))

for i in range(int(input())):
    s, b = input().split()
    if s == 'intersection_update':
        A &= set(map(int, input().split()))
    elif s == 'update':
        A |= set(map(int, input().split()))
    elif s == 'symmetric_difference_update':
        A ^= set(map(int, input().split()))
    else:
        A -= set(map(int, input().split()))
print(sum(A))