query_str = input()
dic = {
    "A": 2, "B": 2, "C": 2, 
    "D": 3, "E": 3, "F": 3,
    "G": 4, "H": 4, "I": 4, 
    "J": 5, "K": 5, "L": 5,
    "M": 6, "N": 6, "O": 6, 
    "P": 7, "Q": 7, "R": 7, "S": 7,
    "T": 8, "U": 8, "V": 8, 
    "W": 9, "X": 9, "Y": 9, "Z": 9
}
sum_value = 0
for v in query_str:
    sum_value += int(dic.get(v)) + 1
print(sum_value)