# Задание 2 Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число: '))
scroll = []


def Factorial(x):
    if x == 1:
        return 1
    else:
        return x * Factorial(x - 1)


for i in range(1, N + 1):
    scroll.append(Factorial(i))

print(scroll)

