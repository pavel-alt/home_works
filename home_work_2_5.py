# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

list_1 = [5, 6, 2, 8, 3, 2, 5, 6, 3, 4]
list_1.sort(reverse=True)
print(list_1)

while True:
    try:
        x = int(input("Стоп-слово '0'\nВведите новый элемент рейтинга: "))
        if x == 0:
            break
        for i in range(len(list_1)):
            if x > list_1[i]:
                list_1.insert(i, x)
                print(list_1)
                break
            elif x <= list_1[-1]:
                list_1.insert(len(list_1), x)
                print(list_1)
                break
    except ValueError as err:
        print(f"Это не натуральное число {err}")
        continue



print(list_1)


# проверять на строго больше чем i-тый элемент массива и вставлять на его место insert'ом