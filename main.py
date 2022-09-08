from random import *
print(randint(1, 100))


for  i in range(2):
    print(randint(10, 150))
a = randint(1, 10)
b = randint(10, 50)
c = randint(a, b)
print(c)


a = int(input('От какого числа загадать число? '))
b = int(input("До какого числа загадать число? "))
c = randint(a, b)
i = 0
while True:
    i+=1
    chislo = int(input('Введите число: '))
    if c>chislo:
        print('Секретное число больше! Попробуйте еще раз!')
    elif c < chislo:
        print('Секретное число меньше! Попробуйте еще раз!')
    else:
        print(f'Поздравляем, вы угадали с {i} попытки!')
        break

