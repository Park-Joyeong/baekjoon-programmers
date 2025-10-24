array_length, target_number = map(int, input().split())
number_array = list(map(int, input().split()))
for _, value in enumerate(number_array):
    if value < target_number:
        print(value, end=" ")