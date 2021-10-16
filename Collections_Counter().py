from collections import Counter

X = int(input())
shoes_size = Counter(list(map(int, input().split())))
N = int(input())
count_money = 0

for _ in range(N):
    size, price = map(int, input().split())
    if size in shoes_size.elements():
        count_money += price
        shoes_size[size] -= 1
print(count_money)