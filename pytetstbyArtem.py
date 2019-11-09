import pytest
import requests
import json

def test_create_role(book_create):
    requests.post(base_url + 'roles/', data={'book': url_1, 'name': 'Artur', 'type': 'Human', 'level': '65'})
    assertEqual(res_1.status_code, 201)
    created_role = res_1.json()
    hero_id = res_1.json()["id"]
    res_2 = requests.get(base_url + 'roles/' + str(hero_id))
    checked = res_2.json()
    assertEqual(created_role, checked)

def test_read_role(role_create):
    res_2 = requests.get(base_url + 'roles/' + str(hero_id))
    checked = res_2.json()
    assertEqual(created_role, checked)

def test_update_role(role_create):
    res_2 = requests.put(base_url + 'roles/' + str(hero_id), data={'type': 'Russo Tagil'})
    assertEqual(res_2.status_code, 200)
    resp_serv_2 = res_2.json()
    res_3 = requests.get(base_url + 'roles/' + str(hero_id))
    resp_serv_3 = res_3.json()
    assertDictEqual(resp_serv_2, resp_serv_3)

def test_delete_role(role_create):
    res_0 = requests.get(base_url + 'roles/' + str(hero_id))
    resp_serv_0 = res_0.json()
    res_2 = requests.delete(base_url + 'roles/' + str(hero_id))
    self.assertEqual(res_2.status_code, 204)
    res_3 = requests.get(base_url + 'roles/' + str(hero_id))
    resp_serv_3 = res_3.json()
    assertIsNot(resp_serv_0, resp_serv_3)