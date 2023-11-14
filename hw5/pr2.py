#Створити структуру даних для студентів з імен та прізвищ, можна випадкових.
# Придумати структуру даних, щоб вказувати, у якій групі навчається
# студент (Групи Python, FrontEnd, FullStack, Java).
# Студент може навчатися у кількох групах. Потім вивести:
# студентів, які навчаються у двох та більше групах
# студентів, які не навчаються на фронтенді
# студентів, які вивчають Python або Java
students = [
{'surname': 'serov', 'name': 'andrey', 'subject':('python', 'full_stack')},
{'surname': 'pupkin', 'name': 'alexander', 'subject':'python'},
{'surname': 'belva', 'name': 'elena', 'subject':('python', 'java', 'front_end', 'full_stack')},
{'surname': 'stepanov', 'name': 'kirill', 'subject':'python'},
{'surname': 'semyonova', 'name': 'alena', 'subject':'front_end'},
{'surname': 'polekhin', 'name': 'ivan', 'subject':'front_end'},
{'surname': 'polekhin', 'name': 'ivan', 'subject':'front_end'},
{'surname': 'kolosov', 'name': 'roman', 'subject':('front_end', 'java', 'full_stack')},
{'surname': 'abrabova', 'name': 'marina', 'subject':'front_end'},
{'surname': 'zharkov', 'name': 'sergei', 'subject':'full_stack'},
{'surname': 'lyubimova', 'name': 'julia', 'subject':'full_stack'},
{'surname': 'doe', 'name': 'john', 'subject':'java'},
{'surname': 'hunt', 'name': 'helen', 'subject':'java'}
]

students_in_multiple_groups = []
for student in students:
     if type(student['subject']) == tuple and len(student['subject']) > 1:
            students_in_multiple_groups.append(student['surname'])
print(f"Студенти, які навчаються у двох та більше групах: {students_in_multiple_groups}")

students_not_in_frontend = []
for student in students:
    if not 'front_end' in student['subject']:
        students_not_in_frontend.append(student['surname'])

print(f"Студенти, які не навчаються на фронтенді: {students_not_in_frontend}")

students_python_or_java = []
for student in students:
    if 'python' in student['subject'] or 'java' in student['subject']:
        students_python_or_java.append(student['surname'])

print(f"Студенти, які вивчають Python або Java: {students_python_or_java}")
