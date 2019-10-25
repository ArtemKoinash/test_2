import requests
import json

import smtplib

url = 'http://pulse-rest-testing.herokuapp.com/'
res = requests.put(url, data={'title':'Green mile', 'author':'king'})
book_credentials = {'title':'Green mile', 'author':'king'}
res_1 = requests.get(url + 'books/', book_credentials)
book_id = res_1.json() # Вот сдесь у меня переменная возвращается как лист а не как словарь который содержит нужный мне id для созданой мною книги. Никак не могу додуматься в чем я ошибся. Что делать дальше я примерно понимаю





# task_2
# output_file_1 = open('fortest.txt', 'w')
# print('Hello my friend!!', file=output_file_1)
# output_file_1.close()
# with open ('fortest.txt', 'w') as ft:
#     ft.write('Tell me story about you')
# # task 3
# input_file = open('text.txt')
# qwer = input_file.read()
# qwer_1 = qwer.split()
# qwer_2 = qwer_1.sort()
# output_file = open('file__to_write.txt', 'w')
# for line in qwer_1:
#     output_file.write(line + qwer_1.count(line) + '\n') # С помощью этого выражения "qwer_1.count(line' пытался вставить число повторения слова в тексте но говрит тчо ошибка, если не сложно обьясните почему
# input_file.close()
# output_file.close()
