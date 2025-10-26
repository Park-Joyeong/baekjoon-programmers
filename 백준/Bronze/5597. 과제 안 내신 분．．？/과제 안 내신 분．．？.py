import sys

student_count = 30
# init
array = [0] * student_count

# 숙제한 사람 기재
for i in range(28):
    student_num = int(input())
    array[student_num - 1] = 1

# 숙제 안 한 사람 출력
for i in range(student_count):
    if array[i] == 0:
        print(i+1, end=' ')