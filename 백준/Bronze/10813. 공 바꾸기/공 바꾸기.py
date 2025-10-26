array_size, swap_count = map(int, input().split())

# init
array = [0] * array_size
for i in range(array_size):
    array[i] = i + 1

# switching loop
for i in range(swap_count):
    start, end = map(int, input().split())
    temp = array[start - 1]
    array[start - 1] = array [end - 1]
    array[end -1] = temp

# print
for i in range(array_size):
    print(array[i], end=' ')