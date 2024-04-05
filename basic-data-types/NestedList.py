if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Sort the list of students based on grades
    students.sort(key=lambda x: x[1])
    
    # Find the second lowest grade
    second_lowest_grade = students[0][1]
    for student in students:
        if student[1] > second_lowest_grade:
            second_lowest_grade = student[1]
            break
    
    # Find students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    
    # Sort and print the names
    for name in sorted(second_lowest_students):
        print(name)
