# Для списка реализовать обмен значений соседних элементов, т.е. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

l1 = []

while True:
    i = input("Введите элемент списка: ")
    if i != "end":
        l1.append(i)
    else:
        break

print(l1)

n = len(l1)

# if n % 2 == 0:
#    for k in range(0, n, 2):
#
# else:
#    for k in range(0, n-1, 2):
#        l1[k], l1[k + 1] = l1[k + 1], l1[k]

for k in range(1, n, 2):
    l1[k], l1[k - 1] = l1[k - 1], l1[k]

print(l1)
