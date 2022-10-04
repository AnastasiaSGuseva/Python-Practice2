# Задание 5 
# Реализуйте алгоритм перемешивания списка.

import random

scroll = [1, 2, 3, 4, 5, 13, 10, 14, 0]
print(scroll)

for i in range(len(scroll)):
    r = random.randrange(0, len(scroll) - 1)
    temp = scroll[i]
    scroll[i] = scroll[r]
    scroll[r] = temp
print(scroll)