import unittest
import requests
import json

class TestBookApi(unittest.TestCase):   #add negative and positive test
    def setUp(self):
        self.url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}

    def test_book_create(self):
        res_1 = requests.post(self.url + 'books/', data=self.book)
        self.assertEqual(res_1.status_code, 201)
        resp_serv_1 = res_1.json()
        self.book['id'] = res_1.json()['id']
        self.assertDictEqual(self.book, resp_serv_1)

    def tearDown(self):
        requests.delete(self.url + 'books/' + str(self.book['id']))

class TestBookRead(unittest.TestCase):
    def setUp(self):
        self.url = url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}
        self.book_post = requests.post('http://pulse-rest-testing.herokuapp.com/books', data=self.book)
        self.book['id'] = self.book_post.json()['id']

    def test_book_read(self):
        res_1 = requests.get(self.url + 'books/' + str(self.book['id']))
        self.assertEqual(res_1.status_code, 200)
        resp_serv_1 = self.book_post.json()
        resp_serv_2 = res_1.json()
        self.assertDictEqual(resp_serv_1, resp_serv_2)

    def tearDown(self):
        requests.delete(self.url + 'books/' + str(self.book['id']))

class TestBookUpdate(unittest.TestCase):
    def setUp(self):
        self.url = url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}
        self.book_post = requests.post('http://pulse-rest-testing.herokuapp.com/books', data=self.book)
        self.book['id'] = self.book_post.json()['id']


    def test_book_update(self):
        res_1 = requests.put(self.url + 'books/' + str(self.book['id']), data={'title': 'Russo turisto'})
        self.assertEqual(res_1.status_code, 200)
        resp_serv_1 = res_1.json()
        res_2 = requests.get(self.url + 'books/' + str(self.book['id']))
        resp_serv_2 = res_2.json()
        self.assertDictEqual(resp_serv_1, resp_serv_2)

    def tearDown(self):
        requests.delete(self.url + 'books/' + str(self.book['id']))

class TestBookDelete(unittest.TestCase):
    def setUp(self):
        self.url = url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}
        self.book_post = requests.post('http://pulse-rest-testing.herokuapp.com/books', data=self.book)
        self.book['id'] = self.book_post.json()['id']

    def test_book_delete(self):
        res_0 = requests.get(self.url + 'books/' + str(self.book['id']))
        resp_serv_0 = res_0.json()
        res_1 = requests.delete(self.url + 'books/' + str(self.book['id']))
        self.assertEqual(res_1.status_code, 204)
        res_2 = requests.get(self.url + 'books/' + str(self.book['id']))
        resp_serv_2 = res_2.json()
        self.assertIsNot(resp_serv_0, resp_serv_2)

    def tearDown(self):
        requests.delete(self.url + 'books/' + str(self.book['id']))

class TestRoleCreate_Read(unittest.TestCase):   #add negative and positive test
    def setUp(self):
        self.url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}
        res = requests.post(self.url + 'books/', data={'title': 'For a character', 'author': 'Steven King'})
        self.book_id = res.json()["id"]
        self.url_1 = 'http://pulse-rest-testing.herokuapp.com/' + 'books/' + str(self.book_id)

    def test_role_create_read(self):
        res_1 = requests.post(self.url + 'roles/', data={'book': self.url_1, 'name': 'Artur', 'type': 'Human', 'level': '65'})
        self.assertEqual(res_1.status_code, 201)
        created_role = res_1.json()
        self.hero_id = res_1.json()["id"]
        res_2 = requests.get(self.url + 'roles/' + str(self.hero_id))
        checked = res_2.json()
        self.assertEqual(created_role, checked)

    def tearDown(self):
        requests.delete(self.url + 'roles/' + str(self.hero_id))
        requests.delete(self.url + 'books/' + str(self.book_id))

class TestRoleUpdate(unittest.TestCase):   #add negative and positive test
    def setUp(self):
        self.url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}
        res = requests.post(self.url + 'books/', data={'title': 'For a character', 'author': 'Steven King'})
        self.book_id = res.json()["id"]
        self.url_1 = 'http://pulse-rest-testing.herokuapp.com/' + 'books/' + str(self.book_id)
        res_1 = requests.post(self.url + 'roles/', data={'book': self.url_1, 'name': 'Artur', 'type': 'Human', 'level': '66'})
        self.hero_id = res_1.json()["id"]

    def test_role_update(self):
        res_2 = requests.put(self.url + 'roles/' + str(self.hero_id), data={'type': 'Russo Tagil'})
        self.assertEqual(res_2.status_code, 200)
        resp_serv_2 = res_2.json()
        res_3 = requests.get(self.url + 'roles/' + str(self.hero_id))
        resp_serv_3 = res_3.json()
        self.assertDictEqual(resp_serv_2, resp_serv_3)


    def tearDown(self):
        requests.delete(self.url + 'roles/' + str(self.hero_id))
        requests.delete(self.url + 'books/' + str(self.book_id))

class TestRoledelete(unittest.TestCase):   #add negative and positive test
    def setUp(self):
        self.url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}
        res = requests.post(self.url + 'books/', data={'title': 'For a character', 'author': 'Steven King'})
        self.book_id = res.json()["id"]
        self.url_1 = 'http://pulse-rest-testing.herokuapp.com/' + 'books/' + str(self.book_id)
        res_1 = requests.post(self.url + 'roles/', data={'book': self.url_1, 'name': 'Artur', 'type': 'Human', 'level': '66'})
        self.hero_id = res_1.json()["id"]

    def test_role_delete(self):
        res_0 = requests.get(self.url + 'roles/' + str(self.hero_id))
        resp_serv_0 = res_0.json()
        res_2 = requests.delete(self.url + 'roles/' + str(self.hero_id))
        self.assertEqual(res_2.status_code, 204)
        res_3 = requests.get(self.url + 'roles/' + str(self.hero_id))
        resp_serv_3 = res_3.json()
        self.assertIsNot(resp_serv_0, resp_serv_3)


    def tearDown(self):
        requests.delete(self.url + 'roles/' + str(self.hero_id))
        requests.delete(self.url + 'books/' + str(self.book_id))

if __name__ == "__main__":
    unittest.main()
#
#
# class TestBookApi(unittest.TestCase):
#     def setUp(self):
#         self.url = url = 'http://pulse-rest-testing.herokuapp.com/'
#          self.book = [ #todo read from file
#             {'title': 'Mama mia', 'author': 'Some Italian'},
#             {'title': 'Mama mia', 'author': 'Some Italian'},
#             {'title': 'Mama mia', 'author': 'Some Italian'},
#             {'title': 'Mama mia', 'author': 'Some Italian'}
#         ]
#


