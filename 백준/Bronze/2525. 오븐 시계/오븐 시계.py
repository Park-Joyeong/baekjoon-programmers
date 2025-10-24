hour, minute = input().split()
hour = int(hour)
minute = int(minute)

add_min = int(input())

total_minutes = hour * 60 + minute + add_min

result_hour = int(total_minutes / 60)
if result_hour >= 24:
    result_hour = result_hour % 24
result_min = total_minutes % 60

print(result_hour, result_min)