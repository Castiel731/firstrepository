#Операторы сравнения, условия if, else, elif
# print (10 == 9)
# print (4 !=5)
# print (10 !=10)
# print ( 10 > 9)

# print ( 10>=10 )
# print (10>=5)

# num1 = int(input('num1: '))
# num2 = int(input('num2: '))
# print (num1+num2)

# name = input ('Введите своё имя:')
# print ('Здравствуйте', name)

# miles = int(input('Введите мили:'))
# print ('Ответ:', miles * 1.609, 'km')

# num1 = int(input('Первая цифра:'))
# num2 = int(input('Вторая цифра:'))
# if num1 > num2:
#     print ('Первая цифра больше')
# else:
#     print ('Вторая цифра больше')

# number1=float(input('Первое число:'))
# operator = input('+, -, /, *:')
# number2 = float(input('Второе число:'))
# if operator == '+':
#     print(number1 + number2)
# elif operator == '-':
#     print(number1 - number2)
# elif operator == '*':
#     print(number1 * number2)
# elif operator == '/':
#     print (number1 / number2)
# else:
#     print('Оператора не существует')

# login = input('Login: ')
# password = input('Password: ')
# if login == 'geektech' and password == 'geektech2021':
#     print ('Welcome')
# else:
#     print('Incorrect password')

# Логические операторы or, and 

# number = int(input('Введите число : '))
# if number < 18:
#     print('Не годен.')
# elif number >= 18 and number <= 27:
#     print ('Годен')
# else: 
#     print('Не годен.')

# num = int(input('Число: '))
# if num % 2==0:
#     print(num,'четный')
# else: 
#     print(num, 'нечетный')
 

import random 
random_number = random.randint(1, 3)
print(random_number)
user_input = input('Введите число: ')
if random_number == user_input:
    print ('win')
else:
    print('lose')

text = 'Hello World'
print(text.count ())