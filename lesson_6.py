#Functions - функции
# def hello_geektech(): 
#     print('Hello World')
#     print('GeekTech')
# # hello_geektech()

# def add():
#     print(111+111)
# add()

# print()


# def add(num1, num2):
#     print (num1+num2)
# add(10, 30)
# add(10, 10)

# def mult(num1:int, num2:int) -> int:
#     print(num1 * num2)
# mult(10, 10)

# def div(num1:int=2, num2:int=2) -> float:
#     print(num1/num2)
# div(40,20)
# div()

# def avg(lst:list) -> int:
#     print(sum(lst)/len(lst))
# numbers = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# nums = [1, 100, 300, 500, 1000, 5000, 10000]
# avg(numbers)
# avg(nums)

# def add(num1:int, num2:int) -> int:
#     print ('Ответ:', num1 + num2)

# def sub(num1:int, num2:int) -> int:
#     print ('Ответ:', num1 - num2)

# def mult(num1:int, num2:int) -> int:
#     print ('Ответ:', num1 * num2)

# def div(num1:int, num2:int) -> int:
#     print ('Ответ:', num1 / num2)

# def main(num1:int, num2:int, operator:str) -> int:
#     if operator == '+':
#         add (num1, num2)
#     elif operator == '-':
#         sub(num1, num2)
#     elif operator == '*':
#         mult(num1, num2)
#     elif operator == '/':
#         div(num1, num2)

# main (20, 30, '+')
# main (10, 5, '-')

# main(20, 30, '+')


# def welcome(name:str) -> str:
#     return 'Здравствуйте ' + name
# print(welcome('Kurmanbek'))

# def info_about_me (name, surname, age, address, language, date_of_birth):
#     print(f"""Всем привет. Меня зовут {name}, а фамилия {surname}. Мне {age} лет.
#     Я живу в {address} и я изучаю язык программирования {language}. Мое день рождение {date_of_birth}""")
# info_about_me('Нурболот','Эркинбаев',18, "Аматов 1Б",'Python', '28 ноября')
# info_about_me('нурислам','эрмегбаев',20,'масалиева 38', 'javascript', '28 ноября')

# Исключение - exceptions 
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print('Деление на ноль невозможно')

# try:
#     print(10 + '10')
# except TypeError:
#     print("TypeError: неподдерживаемые типы операндов для +: 'int' и 'str'")

# try:
#     print(True + 'False')
# except:
#     print('Error')
# finally:
#     print('В итоге я сработаю.')


from modules import add
print(add(30, 40))
