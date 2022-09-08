# def sell(goods, price):
#     print(f'За {goods} товаров заплатите {goods*price} монет')
# sell(5, 10)

# def equate(a, b):
#     c = (a + b * 4) * (a - 3 * b) + a
#     return c
# print(equate(5, 3))


# def smallest(a , b, c):
#     if a>b and c>b:
#         return b
#     elif b>a and c>a:
#         return a
#     else:
#         return c
# print(smallest(1, -2, -3))

# def f(mas):
#     mas  = [*mas[2:], *mas[0:2]]
#     return mas
# print(f([int(i) for i in input().split()]))

# def f(*numbers):
#     n = 0
#     for i in range(1, len(numbers)):
#         if numbers[i]>=numbers[0]:
#             n+=1
#     return f'Экзамен сдали {n} учеников'
# print(f(3, 1, 2, 3, 5, 6, 7))

# print((lambda z, x = 365, y = 687, : z*x//y  )(int(input('Введите количесвто земных лет '))))


