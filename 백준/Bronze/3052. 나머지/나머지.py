result_set = set()
for i in range(10):
    num = int(input())
    modulo = num%42
    result_set.add(modulo)
print(len(result_set))