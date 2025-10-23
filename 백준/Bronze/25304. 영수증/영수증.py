total = int(input())
count = int(input())

calculate = 0
for i in range(count):
    price, cnt = map(int, input().split())
    calculate += price * cnt
if calculate == total:
    print('Yes')
else:
    print('No')