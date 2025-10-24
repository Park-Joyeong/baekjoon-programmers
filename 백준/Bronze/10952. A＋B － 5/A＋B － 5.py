import sys

while True:
    no1, no2 = map(int, sys.stdin.readline().split())
    if no1 == 0 and no2 == 0: break
    print(no1 + no2)
