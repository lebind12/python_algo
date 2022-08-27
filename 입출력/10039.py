students=[]
sum = 0
for i in range(5):
    value = int(input())
    if value < 40:
        value = 40
    students.append(value)
    sum = sum + value
# print(students)
print(sum // 5)