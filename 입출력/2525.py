start_hour, start_min = map(int, input().split(' '))
minute = int(input())

start_min = start_min + minute
start_hour = start_hour + (start_min // 60)
start_min = start_min % 60
start_hour = start_hour % 24

print(str(start_hour) + " " + str(start_min))