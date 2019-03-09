with open('referat.txt', 'r', encoding='utf-8') as file:
	content = file.read()
	count_string = len(content)
	print(f'Длина файла - {count_string} символов!')