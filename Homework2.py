# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке содержащим количество ягод на кустах.


# Input: 2 2 1 3 2
# Output: 7


from random import randint

m = int(input('Введите число кустов: '))
n = int(input('Введите число подряд идущих кустов n: '))

berries = []
for i in range(m):
    berries.append(randint(0,10)) # чтобы не вводить постоянно вручную, максимум 10 взят произвольно


sum = 0
max = 0
print(berries)
for i in range(len(berries)):
    for i in range(n):
        sum = sum + berries[i]
        if sum > max:
            max = sum
    print(sum)
    sum = 0     
    berries.insert(0, berries.pop())
    print()
    print(berries)
print(f'максимальное число ягод с {n} кустов подряд равно {max}')
