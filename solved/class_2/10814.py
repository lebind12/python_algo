import sys


N = int(sys.stdin.readline().rstrip())
people = list()
for _ in range(N):
    age, name = map(str, sys.stdin.readline().rstrip().split(" "))
    person = (int(age), name)
    people.append(person)
people.sort(key=lambda x: x[0])
for i in range(N):
    print(str(people[i][0]) + " " + people[i][1])