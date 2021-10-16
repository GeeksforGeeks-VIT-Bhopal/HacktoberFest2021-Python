input()
s1 = set(input().split())
input()
s2 = set(input().split())

print('\n'.join(sorted((s1 - s2) | (s2 - s1), key=int)))