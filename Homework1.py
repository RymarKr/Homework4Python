# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел.

from random import randint
number1 = int(input('Введите число элементов списка 1: '))
number2 = int(input('Введите число элементов списка 2: '))

plenty1 = []
plenty2 = []

for i in range(number1):
    plenty1.append(randint(0,10))   # чтобы не вводить постоянно вручную, максимум 10 взят произвольно

for i in range(number2):
    plenty2.append(randint(0,10))

result = sorted(list(set(plenty1)&set(plenty2)))

print(plenty1, plenty2)
print(result)