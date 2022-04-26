import base64
import json as j
import uuid

import requests


def login_api(api_url: str, username: str, password: str):
    password_base64_byte = password.encode()
    password_base64_str = base64.b64encode(password_base64_byte)
    end_point = 'login'
    url = api_url + end_point
    headers = {
        "Content-Type": "application/json"
    }
    json = {'username': username, "password": password_base64_str.decode()}

    r = requests.request(method='POST', url=url, headers=headers, json=json)
    token = r.text.replace('Auth_token: ', "")
    return token


def add_to_cart(api_url: str, token: str, product_id):
    headers = {
        "Content-Type": "application/json"
    }
    end_point = 'addtocart'
    url = api_url + end_point
    id = str(uuid.uuid4())
    cookie_str = token.rstrip().replace("\"", "").replace("\"", "")
    json = {"id": id, "cookie": cookie_str, "prod_id": product_id, "flag": 'true'}
    r = requests.request(method="POST", url=url, headers=headers, json=json)
    r.raise_for_status()


def view_cart(api_url: str, token: str):
    headers = {
        "Content-Type": "application/json"
    }
    end_point = 'viewcart'
    url = api_url + end_point
    cookie_str = token.rstrip().replace("\"", "").replace("\"", "")
    json = {"cookie": cookie_str, "flag": 'true'}
    r = requests.request(method="POST", url=url, headers=headers, json=json)
    return j.loads(r.text)


def view_item_info(api_url: str, product_id):
    headers = {
        "Content-Type": "application/json"
    }
    end_point = 'view'
    url = api_url + end_point
    json = {"id": product_id}
    r = requests.request(method='POST', headers=headers, url=url, json=json)
    return j.loads(r.text)
