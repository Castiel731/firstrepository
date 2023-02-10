# Множества set, frozenset
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [3, 4, 5, 6, 7]
# print (set(nums1 + nums2))

# names = {'Kurmanbek', 'Nurbolot', 'Janysh', 'Atai', 'Nurbolot'}
# print(names)
# names.add('Muhtarbek')
# print(names)
# names.remove('Nurbolot')
# print(names)
# names.update('Kurmanbek')
# names.pop()
# print(names)
# for n in names:
#     print (n)

# frzn_set = frozenset({1, 2, 3, 4, 4, 4, 4, 4})
# print(frzn_set)


# Словари - dictionary
# name = {'name' : 'Nurbolot', 'age' : 18}
# print(name)
# name.setdefault('language', 'Python')
# print(name)
# print(len(name))
# print(name['name'])
# print(name['language'])
# name.pop('age')
# print(name)
# name['language'] = "JavaScript"
# print(name)
# name.setdefault('name1','Nurbolot')
# print(name)

games = {'Minecraft' : 2011, 'CS GO' : 2013, 'BeamNG' : 2013}
print(games.values())
print(games.keys())

# for k, v in games.items():
#     print(k, v)

# contact = {'MCHS' : 112}
# while True:
#     command = input('1 - посмотреть контакт, 2 - добавить контакты, 3 - удалить контакты, 4 - обновить контакты: ')
#     if command == '1':
#         print(contact)
#     elif command == '2':
#         add_name = input('Введите имя: ')
#         add_number = input('Введите номер: ')
#         if add_name in contact.keys():
#             print('Такой контакт уже есть')
#         else:
#             contact.setdefault (add_name, add_number)
#             print ('Контакт успешно добавлен')

#     elif command == '3':
#         del_name = input('Кого удалить: ')
#         if del_name in contact.keys():
#             contact.pop(del_name)
#             print('Успешно удалено')
#         else:
#             print('Такого контакта нет')

#     elif command == '4':
#         update_name = input('Кого обновить: ')
#         if update_name in contact.keys():
#             update_number = input('Новый номер: ')
#             contact[update_name] = update_number
#         else: 
#             print('Такого контакта нету')
#     else: 
#         print ('Такой команды нет') 


# import random
# import time
# wins = {}
# games = {}
# n = 0
# random_number = random.randint(1, 10)
# while True:
#     user_number = int(input('Введите число от 1 до 10: '))
#     n += 1
#     if n == 3:
#         print('Вы проиграли всё')
#         games.setdefault(time.ctime(), False)
#         break
#     elif random_number == user_number:
#         print('Вы выиграли. Заполните анкету чтобы получить приз')
#         name = input('Введите имя: ')
#         number = input('Введите номер: ')
#         wins.setdefault(name, number)
#         games.setdefault(time.ctime(), True)
#         print('Успешно добавлено, в течении дня вам позвонят')
#     elif user_number == 777:
#         command = input('1 - посмотреть список выигравших, 2 - посмотреть список игр: ')
#         if command == '1':
#             print(wins)
#         elif command == '2':
#             print(games)
#     else:
#         print('Неправильно у вас', 3 - n, "попыток")


