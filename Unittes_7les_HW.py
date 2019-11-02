import unittest
import requests
import json

class TestBookApi(unittest.TestCase):
    def setUp(self):
        self.url = url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book = {'title': 'Mama mia', 'author': 'Some Italian'}

    def test_book_CRUD(self):
        res_1 = requests.post(self.url + 'books/', data=self.book)
        self.assertEqual(res_1.status_code, 201)
        resp_serv_1 = res_1.json()
        self.book['id'] = res_1.json()['id']
        self.assertDictEqual(self.book, resp_serv_1)
        res_2 = requests.get(self.url + 'books/' + str(self.book['id']))
        self.assertEqual(res_2.status_code, 200)
        resp_serv_2 = res_2.json()
        self.assertDictEqual(resp_serv_1, resp_serv_2)
        res_3 = requests.put(self.url + 'books/' + str(self.book['id']), data={'title': 'Russo turisto'})
        self.assertEqual(res_3.status_code, 200)
        resp_serv_3 = res_3.json()
        res_4 = requests.get(self.url + 'books/' + str(self.book['id']))
        resp_serv_4 = res_4.json()
        self.assertDictEqual(resp_serv_3, resp_serv_4)

    def tearDown(self):
        requests.delete(self.url + 'books/' + str(self.book['id']))



if __name__ == "__main__":
    unittest.main()

# if __name__ == "__main__":
#     from HtmlTestRunner import HTMLTestRunner
#     unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"E:\workspace\test_test"))
