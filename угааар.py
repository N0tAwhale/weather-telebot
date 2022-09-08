"""a = int(input('vveite mark '))
b = int(input('vveite mark '))
c = int(input('vveite mark '))
if all([a>c, b>c]):
    print('c  - min')
elif all([b > a , c > a]):
    print(' a - min')
elif all([a>b, c>b]):
    print('b - min')"""
import random

"""mark = int(input('ocenka '))
if 0<=mark<=40:
    print('ne ochen')
elif 41<=mark<=60:
    print('Not bad')
elif 61<=mark<=80:
    print('Good')
elif 81<=mark<=90:
    print('Great')
else: print('awesome')
"""

"""text = input()
if 'золото' in text:
    print('Yes')
else: print('No')"""

"""text = input()
if 'хорош' in text or 'прекрасн' in text:
    print('Жить хорошо, и жизнь хороша')
elif 'плох' in text:
    print('все будет хорошо... когда-нибудь... наверное...')
elif any(['хорош' not in text, 'плох' not in text, 'не' in text, '?' in text]):
    print('что-то нейтральное')


a , b, c = int(input()), int(input()), input()
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/' and b!=0:
    print(a/b)

else: print('Error 404')"""

"""while True:
    a = int(input('Введите число '))
    if a == 0:
        break"""

from random import *

"""while True:
    print(randint(1, 9))
    a = input('Это твое любимое число?  ')
    if a == 'да': break
    else: continue"""

"""count = 0
while True:
    numb = 0
    count+=1
    numb += count*5
    print(numb)
    if numb == 100: break"""

"""count = 0
a = 1
while count!=10:
    count+=2
    a*=count
print(a)"""

"""strok = input('vvedite ')
while strok !='stop':
    strok = input('vvedite ')
"""

"""count=1
srtok = input()
while srtok != 'Thank you':
    print(srtok)
    count+=1
    srtok = input()
print(count)"""

"""count = 0
temp = float(input('vvedite temp'))
while temp < 22.0:
    temp = float(input('vvedite temp'))
    count += 1 
print('kol polnih nedel ', count//7)"""

"""numb = int(input('vvedite chislo '))
sum = 0
count = 0
while numb !=0:
    count+=1
    sum+=numb
    numb = int(input('vvedite chislo '))
print(sum/count)
"""

"""sum = 0
numb = int(input('vvedite chislo '))
while numb>0:
    if numb>1500:
        numb*=0.92
    sum+=numb
    numb = int(input('vvedite chislo '))
print(sum)"""

"""while True:
    a = input('vvedite parol ')
    b = input('povtorite parol ')
    if all(['123' in a , 'password' in a]):
        print('postoy')
        continue
    elif a!=b:
        print('Razlichautsa')
        continue
    else: print('Ok')"""

"""for  i in range(7, -6, -2):
    print(i)"""
"""sum = 0
proizv = 1
for i in range(1, 11):
    sum+=i
    proizv*=i
print(sum, proizv)"""


"""string = '4###5abn^rrry%5^aaan9@GCddd%M'
count = 0
for i in range(len(string)-1):
    if string[i] == string[i+1] and string[i]==string[i+2]:
        print(string[i])
        count+=1
print(count)"""

"""string = 'hello world!'
for i in range(len(string)-1, 0, -1):
    print(string[i], end='')
"""


"""string = '*'
for i in range(5):
    print(string, end='')
print()
for i in range(20):
    print(string, end = '')
print()

for i in range(10):
    print(string, end = '')

for  i in range (10):
    print()
    for j in range(10):
        print(string, end='  ')
print()

for  i in range (4):
    print()
    for j in range(20):
        print(string, end='  ')"""

"""for i in range (10):
    print()
    for j in range(10):
        print(j, end='')
print()
for i in range (10):
    print()
    for j in range(10):
        print(i, end='')

for i in range (10):
    print()
    for j in range(i):
        print(j, end=' ')
print()
for i in range (10, 0, -1):
    print()
    for j in range(i):
        print(j, end=' ')

print()
count = 0
count_2 = 11
for i in range (10):
    if count == 2 or count == 4:
        text ='пробела  '
    elif count<10:
        text = 'пробелов '
    else:
        text = 'пробелов'
    print()
    for i in range(count):
        print(' ', end='')
    print(f'{count} {text}', end='')
    count += 2
    count_2-=1
    for j in range(0, count_2):
        print(j, end=' ')

for i in range (1, 10):
    print()
    numb = i
    for j in range(9):
        print(i, end=' ')
        i += numb"""


# for i in range(9, 0, -1):
#     a = ''
#     for n in range(i):
#         a+='  '
#     print(a , end='')
#     for j in range(1, 10-i):
#         print(j, end=' ')
#     for k in range(10-i, 0, -1):
#         print(k, end=' ')
#     print()

# print()

# for i in range(9, 0, -1):
#     a = ''
#     for n in range(i):
#         a+='  '
#     print(a , end='')
#     for j in range(1, 10-i):
#         print(j, end=' ')
#     for k in range(10-i, 0, -1):
#         print(k, end=' ')
#     print()
# for i in range(2, 10):
#     a = ''
#     for n in range(i):
#         a+='  '
#     print(a , end='')
#     for j in range(1, 10-i):
#         print(j, end=' ')
#     for k in range(10-i, 0, -1):
#         print(k, end=' ')
#     print()

# string = input('Введите строку ')
# string_2 = input('Введите подстроку ')
# numb = 0
# for i in range(len(string_2) - 1):
#     if string_2[i] == ' ':
#         numb = i
#         break
# print(string.replace(string_2[:numb], string_2[numb + 1:]))

# string = input('Введите строку ').lower()
# if any(['а' not in string, 'б' not in string]):
#     print('error')
# elif string.find('а') < string.find('б'):
#     print('а встречается раньше')
# elif string.find('а') > string.find('б'):
#     print('б встречается раньше')

# string = input('Введите строку ').lower()
# string_2 = ''
# for i in range(len(string)):
#     if string[i] == 'а':
#         string_2 = string.replace('а', 'ая')
# print(string_2.capitalize())


#print(input('Введите строку ').lower().title())


# string = 'йцукенгшщзхъфывапролджэячсмитьбюё'
# string2 = ''
# for i in range(5):
#     string2 = string2 + choice(string) + str(randint(0,9))
# print(string2)


# string = input('Введите строку ')
# if string.count('(') == string.count(')') and string.find('(')<string.find(')'):
#     print('yes')
# else:
#     print('no')

# string = input('Введите строку ').replace(', ', ' ') + ' '
# star = 0
# for i in range(len(string)):
#     if string [i] == ' ':
#         print(string[star:i])
#         star = i+1

# string = input('Введите строку ')
# numb = int(input())
# for i in range(numb):
#     print(string)


# numb = int(input())
# for i in range(numb):
#     string = input('Введите строку ').lower()
#     if 'кот' in string:
#         print('МЯУ')
#         break
#     elif i == 4:
#         print('НЕТ')


# capitals = ['Минск', 'Москва']
# print(*capitals)
# city = input('Введите столицу, которой нет в списке ')
# if city not in capitals:
#     capitals.append(city)
# else: print('Этот город уже имеется')
# for city in capitals:
#     if len(city)<5:
#         capitals.remove(city)
# print(capitals)

# numbers = input().split()
# numb = 1
# for i in range(len(numbers)):
#     numb *= int(numbers[i])
# print(numb)

# name = input().split()
# for i in name:
#     if any([i[0]=='А', i[0]=='О', i[0]=='Е', i[0]=='Э',i[0]=='',i[0]=='Ю',i[0]=='И',i[0]=='Я']):
#         print(i)

# color = input().split()
# for i in range(len(color)):
#     num = i +1
#     print(num, color[i])
#

# numbers =  [int(i) for i in input().split()]
# for i in range(0, len(numbers), 2):
#     print(numbers[i], end = ' ')


# col = int(input())
# numbers =  []
# for i in range(col):
#     numbers.append(randint(0,100))
# print(*numbers)

# numbers =  [int(i) for i in input().split()]
# numb = 1
# if len(numbers) == 0:
#     print(0)
# else:
#     numb *= numbers[1]
# for i in range(0, len(numbers), 2):
#         numb *= numbers[i]
# print(numb)


# numbers =  [int(i) for i in input().split()]
# numbers2 = [int(i) for i in input().split()]
# for numb in numbers:
#     if numb in numbers2:
#         print(numb, end=' ')

# numbers =  [int(i) for i in input().split()]
# numb = int(input())
# n1 =  abs(numbers[0] - numb)
# number = numbers[0]
# for i in numbers:
#     n = abs(i - numb)
#     if n<n1 and number>i:
#         n1 = n
#         number = i
# print(number)

# numbers =  [int(i) for i in input().split()]
# print(max(numbers)-min(numbers))


# numbers = [int(i) for i in input().split()]
# numbers.sort(reverse=True)
# print(*numbers)



# string = list(input().lower())
# a = sorted(string)
# print(a)
# b = 0
# litter = ''
# n = 0
# for i in range(len(a)-1):
#     if a[i]==a[i+1]:
#         n+=1
#         continue
#     elif b<n:
#         b = n
#         litter = a[i]
#         n = 0
# print(litter)


# a = {}
# kol = int(input())
# for i in range(kol):
#     name = input()
#     a[name] = input()
# for key, value in a.items():
#     print(f'Ученик {key} изучает: {value}')

# with open('lol.txt', encoding = 'UTF-8') as file:
#     text = file.read()
#     text2 = text.replace('\n', ' ')
# print(text2)

# with open('lol.txt', encoding = 'UTF-8') as file:
#     text  = file.readlines()
#     alf = 'йукенгшщзхфывапролджжэячсмитьбюё — , '
#     for i in text:
#         print()
#         for j in i.split():
#             j+=' '
#             for n in j:
#                 if n in alf:
#                     print(n, end = '')




# kol = 0
# with open('lol.txt', encoding = 'UTF-8') as file:
#     text = file.readlines()
#     for i in text:
#         kol+=len(i.split())
# print(kol)


# with open('evens.txt', 'w', encoding = 'UTF-8') as file:
#     for i in range(0, 21, 2):
#         file.write(str(i))
#         file.write(' ')

# with open('lol.txt', encoding = 'UTF-8') as file:
#     text = file.readlines()
#     print(text)
# with open('lol.txt', 'a', encoding = 'UTF-8') as file:
#     text_p = input() + '\n'
#     for i in text:
#         if text_p == i:
#             answer = input('Эта строка уже существует. Вы хотите ее добавить? ').lower()
#             if answer == 'да':
#                 print(text_p, file = file)
#                 break
#             else:
#                 break
#         else:
#             print(text_p, file=file)



