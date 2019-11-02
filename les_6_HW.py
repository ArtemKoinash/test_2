import requests
import json
import smtplib
# task_1
# Books
url = 'http://pulse-rest-testing.herokuapp.com/'
res = requests.post(url+ 'books/', data={'title':'Green mile', 'author':'king'})
created = res.json()
book_id = res.json()["id"]
res_1 = requests.get(url + 'books/' + str(book_id))
checked = res_1.json()
if created == checked:
    print("Book was created correctly")
res_2 = requests.put(url + 'books/' + str(book_id), data={'title': 'Shooter on Wild West'})
change = res_2.json()
res_3 = requests.get(url + 'books/' + str(book_id))
checked_2 = res_3.json()
if change == checked_2:
    print("Book was updated")
res_4 = requests.delete (url + 'books/' + str(book_id))
if res_4.status_code < 210:
    print('Book was deleted')
# Roles
res_5 = requests.post(url + 'books/', data={'title':'For a character', 'author':'Steven King'})
book_id2 = res_5.json()["id"]
url_2 = 'http://pulse-rest-testing.herokuapp.com/' + 'books/' + str(book_id2)
res_7 = requests.post(url + 'roles/', data={'book':url_2, 'name':'Artur', 'type':'Human', 'level':'65'})
created_role = res_7.json()
Hero_id = res_7.json()["id"]
res_8 = requests.get(url + 'roles/' + str(Hero_id))
checked_3 = res_8.json()
if created_role == checked_3:
    print('Role was created')
res_9 = requests.put(url + 'roles/' + str(Hero_id), data={'type': 'Super Human'})
change_2 = res_9.json()
res_10 = requests.get(url + 'roles/' + str(Hero_id))
checked_4 = res_10.json()
if change_2 == checked_4:
     print("Role type was updated")
res_11 = requests.delete(url + 'roles/' + '533')
if res_11.status_code < 210:
    print('Role was deleted')
res_12 = requests.delete(url_2)
if res_12.status_code < 210:
    print('Book for role check was deleted')

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
#
# # task_4
#
# email_Obj.starttls()
# email_Obj.login('ArtemKoinashqwerty@ex.ua', 'q123456_')
# to_address = ['Koyansh1@gmail.com', 'Koynash1@i.ua']
# msg_1 = '''\
# From: Artem Koinash
# Subject: Home Work
# Hope i did it'''
#
# email_Obj.send_message(msg="i did it", from_addr='ArtemKoinashqwerty@ex.ua', to_addrs='koinash1@gmail.com')
# email_Obj.quit()
#
