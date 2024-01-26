# I was using a little bit of this tutorial while doing this task:
# https://www.freecodecamp.org/news/how-to-use-the-json-module-in-python/
import json
import numpy as np

with open("students_data.json", "r") as f:
    data = json.load(f)


# sum of all the grades
def sum_grades(students):
    """
    Function calculating sum of all the grades achieved by all the students.
    :param students: (json data) JSON-format list of all the students.
    :return grades: (int) Sum of all the grades achieved by all the students.
    """
    grades = [student["grades"] for student in students]
    grades = np.sum(grades)
    return grades


# calculating the grade
def calculate_average_grade(students):
    """
    Function calculating average of all the grades achieved by all the students.
    :param students: (json data) JSON-format list of all the students.
    :return averaged_grades: (float) Average of all the grades achieved by all the students.
    """
    grades = sum_grades(students)
    number_of_grades = 0
    for student in students:
        number_of_grades += len(student["grades"])
    averaged_grades = np.sum(grades)/number_of_grades

    return averaged_grades


def filter_top_students(students):
    """
    Function returning all the students from the JSON-format data whose average grade is higher than 85.
    :param students: (json data) JSON-format list of all the students.
    :return: (list of json objects) List of JSON objects representing data of all the students whose average grade is
            higher than 85.
    """
    top_students = list(filter(lambda student: np.average(student['grades']) > 85, students))
    return top_students


def count_top_students(students):
    """
    Function returning number of students whose averaged grade is higher than 85.
    :param students: (json data) JSON-format list of all the students.
    :return: (int) Number of students whose averaged grade is higher than 85.
    """
    criteria_avg_grade = 85
    over_criteria_students = list(map(lambda student: np.average(student['grades']) > criteria_avg_grade, students))
    number_of_students = 0
    for i in over_criteria_students:
        if over_criteria_students[i]:
            number_of_students += 1
    return number_of_students


def top_10_scores(students):
    """
    Function returning top 10 students which the highest averaged grade.
    :param students: (json data) JSON-format list of all the students.
    :return: (list of json objects) List of JSON objects with data of all the students whose average grade is in top 10
             of all the students.
    """
    sorted_student = sorted(students, key=lambda student: np.average(student['grades']), reverse=True)
    return sorted_student[:10]


print('Sum of grades of all the students:', end=" ")
print(sum_grades(data))
print('===========================')
print('Average grade of all the students:', end=" ")
print(calculate_average_grade(data))
print('===========================')
print('Top students (average grade > 85):', end="")
print(filter_top_students(data))
print('===========================')
print('Number of students fulfilling certain condition (average grade > 85):', end=" ")
print(count_top_students(data))
print('===========================')
print('Top 10 students with the best scores:', end=" ")
print(top_10_scores(data))
print()
