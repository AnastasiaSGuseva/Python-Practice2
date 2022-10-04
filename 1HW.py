# Задание 1 Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11

Number = input('Введите число: ')
a = len(Number)
sum = 0

for i in range(a):
    if Number[i].isdigit():
        c = int(Number[i])
        sum = sum + c
    else:
        i+=1
print('Сумма равна', sum)