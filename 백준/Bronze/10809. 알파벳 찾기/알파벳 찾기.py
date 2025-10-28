param_str = input()
param_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result_array = []

for i, value in enumerate(param_array):
    idx = param_str.find(value)
    result_array.append(idx)

for _, value in enumerate(result_array):
    print(value, end=' ')