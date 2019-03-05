# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
#ИЛИ
#last_symbol = None
#for symbols in word:
	#last_symbol = symbols
#print(last_symbol)


# Вывести количество букв а в слове
word = 'Архангельск'
a = word.count('А')
b = word.count('а')
c = a+b
print(c)


# Вывести количество гласных букв в слове
CONS_lower = "бвгджзклмнпрстфхцчшщ"
cons_lower_List = list(CONS_lower)
CONS_upper = CONS_lower.upper()
cons_upper_List = list(CONS_upper)

counter = 0
word = 'РАрхангельск'
for letter in word:
	if letter in cons_lower_List or letter in cons_upper_List:
		counter += 1
print(counter)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
splited_sentence = sentence.split()
for words in splited_sentence:
	print(words[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
count_words = len(sentence.split())
count_letters = len(sentence) - sentence.count(' ')
print(count_letters // count_words)
	



