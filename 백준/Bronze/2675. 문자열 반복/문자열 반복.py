loop_count = int(input())

for _ in range(loop_count):
    repeat_count, target_str = input().split()
    repeat_count = int(repeat_count)
    for i, value in enumerate(target_str):
        print(value * repeat_count, end="")
    print()
