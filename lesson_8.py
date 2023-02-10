# Модули 
# import modules 
# print(modules.count_points('Atai', 5, 5, 5, 5, 5, 4, 4, 4))

# print(modules.name)
# print(modules.numbers)

# Второй способ 

# from modules import count_points
# print(count_points('Janyshbek', 4, 4, 4, 4, 4, 5, 5, 5, 5))


# # Третий способ
# from modules import *
# print(count_points('Muhtarbek', 5, 5, 5, 5, 5, 5))

# Работа с файлами
# f = open('hello.txt', 'w')
# f.write('Hello geeks')
# f.close()
 
# r = open('hello.txt', 'r')
# print(r.read())
# r.close()

# password = open('password.txt', 'a+')
# password.write('Hello\n')
# password.write('World')
# password.close()


# with open('geeks.txt', 'a+') as g:
#     g.write('How are you?')     

import random
def generate_passwords(lens_password:int, count_password:int):
    letters = '1234567890qwertyuiopasdfgjhk!@#$%^&&*'
    lst_letters = []
    for i in letters:
        lst_letters.append(i)
    print(lst_letters)
    for n in range(count_password):
        res = ''
        for l in range(lens_password):
            res += random.choice(lst_letters)
        with open('passwords.txt', 'a+') as p:
            p.write(f"{res}\n")
        print(res)
generate_passwords(10, 8)

