loop_count = int(input())
for _ in range(loop_count):
    param_str = input()
    print(param_str[0], end='')
    print(param_str[len(param_str) - 1], end='')
    print()