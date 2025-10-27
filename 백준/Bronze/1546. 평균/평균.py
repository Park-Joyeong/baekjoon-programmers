score_size = int(input())
score_array = []
max = 0

# 점수 입력받기
score_array = list(map(int, input().split()))
for i in range(score_size):
    score = score_array[i]
    if score > max:
        max = score

# 점수 조작
for i in range(score_size):
    score_array[i] = score_array[i] / max * 100

print(sum(score_array) / score_size)