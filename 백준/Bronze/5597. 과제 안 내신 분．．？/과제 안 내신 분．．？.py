allStudents = []

for student in range(1, 31):
    allStudents.append(student)

for num in range(1,29):
    student = int(input(""))
    allStudents.remove(student)

allStudents.sort()

print(allStudents[0])
print(allStudents[len(allStudents)-1])

    
