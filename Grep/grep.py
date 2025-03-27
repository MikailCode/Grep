def files(arg, string, level):
	my_file = rf'{arg}'
	with open(my_file, 'r') as file:
		lst = file.readlines()
		array_file = [i.strip().split() for i in lst]
		array_file1 = [j.strip() for j in lst]
	if level == '1':
		for i in array_file:
			if string in i:
				print(' '.join(i))
	if level == '2':
		for k in array_file1:
			if string in k:
				print(k)

files(input('Укажите путь до файла: \n'), input('Укажите слово, какие строки будем искать: \n'), input('Укажите уровень точности поиска: 1(Полная строка) or 2(Ищет даже по буквам): \n'))