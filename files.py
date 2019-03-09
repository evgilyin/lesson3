#Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
with open('referat.txt', 'r', encoding='utf-8') as file:
	content = file.read()
	count_symbols = len(content)
	print(f'Длина файла - {count_symbols} символов!')

#Подсчитайте количество слов в тексте
	count_words = len(content.split())
	print(f'Количество слов в тексте - {count_words}!')

#Замените точки в тексте на восклицательные знаки
	replace_symbols = content.replace('.', '!')
	print(replace_symbols)
	
#Сохраните результат в файл referat2.txt
with open('referat2.txt', 'w', encoding='utf-8') as file:
	file.write(replace_symbols)
