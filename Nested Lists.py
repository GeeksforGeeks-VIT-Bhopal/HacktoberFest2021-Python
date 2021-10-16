from decimal import Decimal
from itertools import groupby, islice
from operator import itemgetter

a = []
for i in range(int(input())):
  x, y = (input(), Decimal(input()))
  a.append((y, x))
a.sort()
for k, v in islice(groupby(a, key=itemgetter(0)), 1, 2):
  for x in v:
    print(x[1])