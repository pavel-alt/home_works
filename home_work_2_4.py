# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_list = input("Введи произвольную строку с пробелами и пусть тебе поможет Босх: ").split(" ")
i = 0
for el in user_list:
    i += 1
    print(i, el[0: 10])
# Разобрать и запомнить метод.

user_list2 = [int(i) + 1 for i in input("Введи произвольную строку с пробелами и пусть тебе поможет Босх: ").split(" ")]

print(user_list2)
