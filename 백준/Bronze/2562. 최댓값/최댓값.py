max_value = 0
max_position = 1
for i in range(1, 10):
    num = int(input())
    if (num > max_value):
        max_value = num
        max_index = i
print(max_value)
print(max_index)