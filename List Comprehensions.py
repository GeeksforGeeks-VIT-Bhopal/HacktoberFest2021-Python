X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

X += 1
Y += 1
Z += 1

tmp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(tmp_list)