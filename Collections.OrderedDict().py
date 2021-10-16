
from collections import OrderedDict
my_order = OrderedDict()
for i in range(int(input())):
    name,space,price = input().rpartition(' ')
    if name not in my_order:
        my_order[name] = int(price)
    else:
        my_order[name] += int(price)
for item_name, net_price in my_order.items():
    print(item_name,net_price)
