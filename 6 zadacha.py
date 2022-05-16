#Задача №6
#Найти сумму цифр числа
n = int(input('Введите число: '))
s = 0
while n > 0:
    count = n % 10
    s += count
    n //= 10
print("Сумма цифр:", s)
