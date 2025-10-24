import sys

loop_count = int(sys.stdin.readline())
for i in range(loop_count):
    no1, no2 = map(int, sys.stdin.readline().split())
    print(f'Case #{i + 1}: {no1 + no2}')
