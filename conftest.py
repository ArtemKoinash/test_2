import requests
import json
import pytest
base_url  = 'http://pulse-rest-testing.herokuapp.com/'
book = {'title': 'Mama mia', 'author': 'Some Italian'}

@pytest.fixture()
def role_create():
    res = requests.post(base_url + 'books/', data={'title': 'For a character', 'author': 'Steven King'})
    book_id = res.json()["id"]
    url_1 = base_url + 'books/' + str(book_id)
    res_1 = requests.post(base_url + 'roles/', data={'book': url_1, 'name': 'Artur', 'type': 'Human', 'level': '66'})
    hero_id = res_1.json()["id"]

@pytest.fixture()
def role_delte():
    requests.delete(base_url + 'roles/' + str(hero_id))
    requests.delete(base_url + 'books/' + str(book_id))

@pytest.fixture()
def book_create():
    book_post = requests.post(base_url + 'books', data=book)
    book['id'] = book_post.json()['id']



@pytest.fixture()
def book_delte():
    requests.delete(base_url + 'books/' + str(book['id']))

