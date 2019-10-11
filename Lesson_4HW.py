# task_1
# def song(string = 3, words = 3, end = 0): #додумался пока что как реализовать 2 аргумент
#     """this function should return song 'la-la-la', where:
#         string - is a number of strings, by default 3
#         words - is number of 'La' in each  string, by default 3
#         end - is last sign in a last string '.' if end = 0 or '!' if end = 1, by default '.'"""
#     if words == 0:
#         return "none"
#     else:
#         return "la - " * (words - 1) + "la"
#     if string == 0:
#         return "none"
#     else:
#         return words * string
#
#     # if
# print(song(string = 2, words = 3))

# # task_2
# """ths function should show second value by increase from values that was inputed in function"""
# def biggest (*numbers):
#     q = set(numbers)
#     q1 = list(q)
#     q1.sort()
#     return q1[1]
# print(biggest(34, 56, 234, 435, 12346, 16, 16, 8, 8 , 8, 12, 12))


# # task_3 пока не додумался как реализовать, еще буду думать :)
# def digit_delete(*characters):
#     w = str(characters)
#     e = "1234567890"
#     for char in e:
#         w = w.replace(char, "")
#     return w
#
# print(digit_delete(dg00tts987tystdgh45dgtxfg1345))


# # task_4.1
# list1 = [2**N for N in range(20)]
# print(list1)
# # task_4.2
# list2 = [i % 3 for i in list1]
# print(list2)
# # task_4.3 пока не додумался как реализовать, еще буду думать :)
# list3 = [12, 534, 'retro', '31', 'er', ['fasso', 324, '343']]
# # task_4.4 пока не додумался как реализовать, еще буду думать :)
# list4 = [ for i in list3]
# print(list4)

