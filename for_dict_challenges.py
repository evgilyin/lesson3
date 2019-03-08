# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]


students_count = dict()
for student in students:
	name = student['first_name']
	if name not in students_count:
		students_count[name] = 1
	else: 
		students_count[name] = students_count[name] + 1



for students in students_count:
	print(f'{students}: {students_count[students]}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

students_count = dict()
max_frequency = 0
frequency_name = []


for student in students:	
	name = student['first_name']
	if name not in students_count:
		students_count[name] = 1
	else: 
		students_count[name] = students_count[name] + 1
	
	if students_count[name] > max_frequency:
		max_frequency = students_count[name]
		frequency_name = [name,]
	elif students_count[name] == max_frequency:
		max_frequency = students_count[name]
		frequency_name.append(name)


print(f"Самые частые имена: {(', '.join(frequency_name))}")



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Оля'}
  ]
]

class_number = 0

for classes in school_students:
	students_count = dict()
	max_frequency = 0
	frequency_name = []
	for students in classes:
		name = students['first_name']
		if name not in students_count:
			students_count[name] = 1
		else: 
			students_count[name] = students_count[name] + 1
	
		if students_count[name] > max_frequency:
			max_frequency = students_count[name]
			frequency_name = [name,]
		elif students_count[name] == max_frequency:
			max_frequency = students_count[name]
			frequency_name.append(name)
	class_number += 1
	print(f"Самые частые имена в классе {class_number}: {(', '.join(frequency_name))}")



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for classes in school:
	girls = 0
	boys = 0
	for students in classes['students']:
		name = students['first_name']
		if is_male[name] == False:
			girls += 1
		elif is_male[name] == True:
			boys += 1
	print(f"В классе {classes['class']} {girls} девочек и {boys} мальчиков")
		


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for classes in school:
	girls = 0
	boys = 0
	max_boys = 0
	max_girls = 0
	max_boys_class = []
	max_girls_class = []
	for students in classes['students']:
		name = students['first_name']
		if is_male[name] == False:
			girls += 1
		elif is_male[name] == True:
			boys += 1

		if girls >= max_girls:
			max_girls = girls
			max_girl_class = [classes['class'],]
		if boys >= max_boys:
			max_boys = boys
			max_boys_class = [classes['class'],]
	print(f"Больше всего мальчиков в классе {(', '.join(max_boys_class))}")
	print(f"Больше всего девочек в классе {(', '.join(max_girls_class))}")
