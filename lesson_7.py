# #Лямда, lambda функции.
# def two_mult(x:int) -> int:
#     return x * x
# print(two_mult(10))


# lambda_two = lambda x: x * x
# print(lambda_two(10))

# print((lambda x: x * x)(10))


# Пример 2 
# def add (num1, num2):
#     return num1 + num2 
# print(add(20, 20))


# lambda_add = lambda num1, num2: num1 + num2
# print(lambda_add(20, 20))



# print((lambda num1, num2: num1 + num2)(20, 20))


# Пример 3
# numbers = [10, 20, 30, 40, 50]
# result = []
# def two_mult_list(nums:list) -> list:
#     for i in nums:
#         result.append(i * 2)
#     return result
# print(two_mult_list(numbers))

# numbers = [10, 20, 30, 40, 50]
# lambda_mult_list = list(map(lambda nums: nums * 2, numbers))
# print(lambda_mult_list)


# numbers = [10, 20, 30, 40, 50]
# print(list(map(lambda nums: nums * 2, numbers)))

# print(list(map(lambda nums: nums * 2, [10,20,30,40,50])))



# Пример 4
# numbers = [1,2,3,4,5,6,7,8,9,10]
# chet = []
# def count_chet(nums:list) -> list:
#     for i in nums:
#         if i % 2 == 0:
#             chet.append(i)
#     return chet 
# print(count_chet(numbers))
# #################################
# numbers = [1,2,3,4,5,6,7,8,9,10]
# chet = list(filter(lambda nums: nums % 2 == 0, numbers))
# print(chet)
# ############################################################
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda nums: nums % 2 == 0, numbers)))
# ###########################
# print(list(filter(lambda nums: nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# def employee(name1, name2):
#     print('ЗДравствуйте', name1)
#     print('ЗДравствуйте', name2)
# employee('Atai', 'Janyshbek', 'Muhtarbek', 'Kurmanbek')

# def employee(*names):
#     for name in names:
#         print('Здравствуйте', name)
# employee('Atai', 'Janyshbek', 'Muhtarbek', 'Kurmanbek')


# def output_point(name, *points):
#     print(name, sum(points) / len(points))
# output_point('Nurbolot', 4, 4, 4, 3, 3, 3, 5, 5, 5)

# def translate(**words):
#     print(words)
# translate(USA='США', apple = 'Яблоко')