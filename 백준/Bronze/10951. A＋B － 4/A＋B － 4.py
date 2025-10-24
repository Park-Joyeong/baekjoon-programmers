import sys

while True:
    try:
        no1, no2 = map(int, input().split(' '))
        print(no1 + no2)
    except:
        break