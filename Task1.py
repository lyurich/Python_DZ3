# Задаем длину списка наполненного рандомными числами от 1 до 100. Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению.
import sys
from random import randint
import time

length = int(input('Введите длину списка: '))
number = int(input('Введите искомое число: '))
my_list = []
for _ in range(length):
    my_list.append(randint(1, 20))
print(my_list)

count = 0

for i in range(length):
    if my_list[i] == number:
        count += 1
        print(f'Искомое число встречается {count} раз')
        sys.exit()


nearest_number = my_list[0]
for i in range(length):
    if abs(my_list[i] - number) < abs(nearest_number - number) or abs(my_list[i] - number) == abs(nearest_number - number) and my_list[i] < nearest_number:
        nearest_number = my_list[i]
print(f'Ближайшее число = {nearest_number}')




