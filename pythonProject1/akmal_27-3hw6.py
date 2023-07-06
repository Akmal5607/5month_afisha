# def multiply1(numbers):
#     counter = 1
#     for number in numbers:
#         counter *= number
#     return counter
# print(multiply1([2, 3, 4, 5]))
#
# def multiply(*args):
#     return multiply1(args)
# print(multiply(2, 3, 4, 5))



# def calculator(n1, operator, n2):
#     if operator == '+':
#         return n1 + n2
#     elif operator == '-':
#         return n1 - n2
#     elif operator == '**':
#         return n1 ** n2
#     elif operator == '%':
#         return n1 % n2
#     elif operator == '/':
#         return n1 / n2
#     else:
#         print('Неверно')
#
# print(calculator(2, '**' ,3))
# print(calculator(5, '+' , 9.6))
# print(calculator(10, 'плюс', 5))
# print(calculator(20, '%' ,3))
# print(calculator(30, '/' ,2))
# print(calculator(10, '-' ,5))





# def is_mirror(string, hello='unknown'):
#     if string == string[::-1]:
#         return True
#     elif string == string:
#         return False
#     else:
#         return hello
#
# print(is_mirror('dovod'))
# print(is_mirror('python'))

