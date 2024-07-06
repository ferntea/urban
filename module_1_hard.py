# module_1_hard

'''
Задание "Средний балл":
Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого
ученика, поэтому вам предстоит автоматизировать этот процесс":

На вход даны следующие данные:
    Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
    Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

    Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
    Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
'''

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_list = sorted(list(students))
# print(student_list)

student_grades_dict = {}
student_grade_av_dict = {}
for i in range(len(student_list)):
    student_grades_dict[student_list[i]] = grades[i]

print(student_grades_dict)

for i in range(len(student_list)):
    student = student_list[i]
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    student_grade_av_dict[student] = average_grade

print(student_grade_av_dict)


