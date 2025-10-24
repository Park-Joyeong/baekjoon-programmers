hour, minute = input().split()
hour = int(hour)
minute = int(minute)


total_minute = hour * 60 + minute

total_minute -= 45
if total_minute < 0:
    total_minute += 1440

result_hour = int(total_minute / 60)
result_minute = total_minute % 60
print(result_hour, result_minute)