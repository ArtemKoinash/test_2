#task 1:
# q = input('enter smth: ')
# print(q[2])
# print(q[-2])
# print(q[:6])
# print(q[:-2])
# print(q[::2])
# print(q[1::2])
# print(q[::-1])
# print(q[::-2])
# print(q[-2::-2])
# print(q[-2:0:-1])
# print(len(q))
#выловить исключениея если строка слишком короткая - не додумался какой имено експшеннужно

#task_2 нашел решение в сети но не понял его
# s = input("enter smt:  ")
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

# #task _3.1
# i = 0
# while i < 11:
#     print (i)
#     i = i + 1

# #task_3.2
# u = 20
# while u >= 1:
#     print(u, end=' ')
#     u = u - 1

# #task_3.3
# x = int(input('enter number: '))
# counter = 0
# while x % 2 == 0:
#     print(x)
#     counter += 1
#     if x % 2 != 0:
#         break
#     x /= 2
# print(counter)

# task_4 не успел разобраться
# task_5 не успел разобраться

# #task_6.3
# def is_leap_year (y):
#     if int(y) % 4 != 0 or (int(y) % 400 != 0 and int(y) % 100 == 0):
#         print("false")
#     else:
#         print("true")
# y = int(input('type any year: '))
# is_leap_year(y)

# #task_6.3
# def triangle (a, b, c):
#     if a < b + c and b < a + c and  c < a + c:
#         print('true')
#     else:
#         print('false')
# triangle (12, 23, 10)

# #task_6.5
# def triangle_type (a, b, c):
#     if a > b + c or b > a + c or c > a + c:
#         print('false')
#     elif a == b == c:
#         print('Equilateral triangle')
#     elif a == b or a == c or b == c:
#         print('Isosceles triangle')
#     else:
#         print('Versatile triangle')
# triangle_type (17, 10, 15)

# #task_6.6
# x1 = float(input('enter some number: '))
# y1 = float(input('enter some number: '))
# x2 = float(input('enter some number: '))
# y2 = float(input('enter some number: '))
# def distance (x1, y1, x2, y2):
#     return ((x2-x1)**2 + (y2 - y1)**2)**0.5
# print(distance(x1, y1, x2, y2))

# #task_7 не во всем разобрался пока что
# text = "We are not what we should be!\nWe are not we need to be.\nBut a t least we are not what we used to be\n(Football Coach)"
# t = text.split()
# len(t)

