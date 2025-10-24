count = int(input())
array = list(map(int, input().split()))
min = array[0]
max = array[0]
for i, value in enumerate(array):
    if (value < min):
        min = value
    if (value > max):
        max = value
print(min, max)
    