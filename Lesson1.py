# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:       6 -> да
#               7 -> да
#               1 -> нет

# day = int(input('Введите номер дня недели: '))
# if day > 7 or day < 1:
#     print('Введите число от 1 до 7')
# elif day == 6 or day == 7:
#     print('Выходной день')
# else:
#     print('Будний день')


# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range (0, 2):
    for y in range (0,2):
        for z in range (0,2):
            print(not(x or y or z) == (not x and not y and not z))