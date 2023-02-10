# Tuple - Кортежи
# it_company = ('GeekTech', 'GeekStudio', "MadDevs")
# print (it_company)
# tup = (10, 2.0, True, 'Geek')
# print (tup)
# print(it_company.count('GeekTech'))
# print(it_company.index('MadDevs'))
# print(it_company)

# lst_company = list(it_company)
# print(lst_company)
# lst_company.append("Hapsida")
# print(lst_company)
# it_company = tuple(lst_company)
# print(it_company)

# tup = (10, 33.3, 'Hello', False, (1, 2, 3, 4,), [1, 2, 3])
# print(tup)

# tup = ('Hello',)
# print(type(tup))
# 
# 

# for i in range(10, 20, 1):
#     print(i)

# numbers = [10, 2, 3, 4, 5, 73, 101, 203, 1001, 4403]
# for num in numbers:
#     if num % 2 == 0:
#         print (num, 'четный')
#     else:
#         print (num, 'нечетный')

# names = ['Kurmanbek', 'Nurbolot', 'Atai', 'Janysh', 'Muhtarbek']
# for name in names:
#     print(name)


# cars = ('BMW', 'MERCEDES', 'TESLA', 'HONDA')
# for car in cars:
#     print (car)

# geek = 'GeekTech'
# for g in geek:
#     print (g)


# num = 23
# for n in num:
#     print (n)


# numbers = [100, 101, 102, 103, 200, 204]
# for n in numbers:
#     if n == 200:
#         print('OK')
#         continue
#     print (n)
    


# nums = []
# for i in range (1, 101):
#     nums.append(i)
# print(sum(nums))

# num1 = 10
# num2 = 20
# while num2 > num1:
#     num1 += 1
#     print (num1)


# n = 0
# while True:
#     n += 1
#     print(n)
#     if n == 10000:
#         print('Stop')
#         break

# import random
import time 
# i = 0
# random_number = random.randint(1000, 9999)
# i = 0
# while True:
#     time.sleep(0.1)
#     i += 1
#     if i == random_number:
#         print ('''Hacked.''', random_number, 'is password')
#         break
#     print('Hacking', i)

while True:
    time.sleep(1)
    print(time.ctime())


