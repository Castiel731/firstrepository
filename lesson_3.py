#str - строки 
# name = 'Kurmanbek. I\'m backend developer'  
# print(type(name))
# name = "Kurmanbek. I'm backend developer \n Language Python"
# print(name)
# name = """Kurmanbek. I'm backend developer
# Language Python"""

# geek = "geektech"
#        #01234567   
# print (geek[0]) #Получение буквы по индексу 
# print (geek[0:4]) #Срезы
# print (geek[4:8]) #Срезы
# print (geek[0:4:2]) #Срезы с шагами

#Lists - списки 
# lst = [1, 20.0, "Hello", True]
# print (lst)

# name1 = "Nurbolot"
# name2 = "Arsen"
# name3 = "Bayastan"
# print(name1)
# print(name2)
# print(name3)

# names = ["Nurbolot", "Arsen", "Bayastan"]
# print (names)
# names.append('Atai')
# print(names)
# names.append('Janysh')
# print(names)
# names.remove("Arsen")
# print(names)
# print ([names[2]])
# print(names[0][0])
# names[0] = 'Bolot'
# print(names)

# cars = ["BMW", "TESLA", "HONDA"]
# cars.insert(2, "LOTUS")
# print(cars)
# cars.pop(0)
# print(cars)
# print(cars.index("HONDA"))
# print(cars.count('TESLA'))
# cars.clear()
# print(cars)

# numbers = [10, 1, 111, 114, 1000, 5000, 404, 500, 0.1]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# lst = [2.0, 44, 'World', False, [1, 2, 3, 4, 5]]
# print(lst[4][2])

contacts = ['112']
while True:
    commands = input('Введите комманду 1 - искать, 2 - добавлять, 3 - удалять, 4 - обновлять, 5 - посмотреть контакты: ')
    if commands == '1':
        find = input('Кого искать: ')
        if find in contacts:
            print(find, 'найден')
        else:
            print(find, 'не найдеен')
    elif commands == '2':
        add = input('Кого добавлять: ')
        contacts.append(add)
        print('Успешно добавлено')
    elif commands == '3':
            delete = input('Кого удалить: ')
            contacts.remove(delete)
            print('Успешно удалено')
    elif commands == '5':
            print(contacts)
    elif commands == '4':
        update = input('Кого обновить: ')
        update_index = contacts.index(update)
        new_update = input('Новое имя: ')
        contacts[update_index] = new_update
        print('Успешно обновлено')
    elif commands == '5':
        print(contacts)
    else:
        print('Такой команды нету')