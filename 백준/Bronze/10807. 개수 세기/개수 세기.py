array_length = int(input())
array = input().split()
target_number = int(input())
result_count = 0
for i in range(array_length):
    if int(array[i]) == target_number:
        result_count += 1
print(result_count)