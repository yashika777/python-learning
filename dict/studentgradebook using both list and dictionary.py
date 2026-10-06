#  Student Grade Book (Dictionary + List)
# Complete student management system:
# python# Grade book structure
# gradebook = {
#     "Raj": [85, 90, 88],
#     "Priya": [92, 88, 95],
#     "Amit": [78, 82, 80]
# }
# Features to implement:
# 1. Add new student with marks
# 2. Add marks to existing student
# 3. Calculate average for each student
# 4. Find student with highest average
# 5. Display all students and their averages
# 6. Grade classification (A: >90, B: 80-90, C: 70-80, F: <70)
# **Sample Output:**
gradebook = {
    "Raj": [85, 90, 88],
    "Priya": [92, 88, 95],
    "Amit": [78, 82, 80]
}
def calculate_averages():
    average = {}
    for student, marks in gradebook.items():
        total = 0
        for mark in marks:
            total += mark
        average[student] = total / len(marks)
    return average
while True:
    print("""
------ Student Grade Card ------
1). Add new student with marks
2). Add marks to existing student
3). Calculate average for each student
4). Find student with highest average
5). Display all students and their averages
6). Grade classification
7). Exit
""")
    enter = int(input("Enter choice: "))
    if enter == 1:
        name = input("Enter name: ")
        marks = []
        for i in range(3):
            mark = int(input("Enter marks: "))
            marks.append(mark)
        gradebook[name] = marks
    elif enter == 2:
        student = input("Enter name of existing student: ")
        if student in gradebook:
            mark = int(input("Enter marks: "))
            gradebook[student].append(mark)
        else:
            print("Invalid name!!")
    elif enter == 3:
        average = calculate_averages()
        for student, avg in average.items():
            print(student, ":", round(avg, 2))
    elif enter == 4:
        average = calculate_averages()
        highest = 0
        student = ""
        for name, avg in average.items():
            if avg > highest:
                highest = avg
                student = name
        print("Highest average:", student, ":", round(highest, 2))
    elif enter == 5:
        average = calculate_averages()
        for student, avg in average.items():
            print(student, ":", round(avg, 2))
    elif enter == 6:
        average = calculate_averages()
        for student, avg in average.items():
            if avg > 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            else:
                grade = "F"
            print(student, ":", grade)
    elif enter == 7:
        print("Exiting...... bye bye")
        break
    else:
        print("Invalid!!!!!")


        
           



                

