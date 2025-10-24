basket_count, put_count = map(int, input().split())

result_array = [0] * basket_count
for i in range(put_count):
    start_position, end_position, value = map(int, input().split())
    for j in range(start_position - 1, end_position):
        result_array[j] = value
for _, value in enumerate(result_array):
    print(value, end=' ')