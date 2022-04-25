from . import api
from .api_helper import get_username_from_file

API_URL = 'https://api.demoblaze.com/'
ITEM_ID = '3'
LOGIN = get_username_from_file()
PASSWORD = '111'

def test_add_item_to_cart():
    print(LOGIN)
    token = api.login_api(api_url=API_URL, username=LOGIN, password=PASSWORD)
    api.add_to_cart(api_url=API_URL, token=token, product_id=ITEM_ID)

    items_in_cart = api.view_cart(api_url=API_URL, token=token)
    assert items_in_cart['Items'][0]["prod_id"] == ITEM_ID
    assert len(items_in_cart['Items']) == 1

    item_info = api.view_item_info(api_url=API_URL, id=ITEM_ID)
    assert item_info['title'] == 'Nexus 6'
    assert item_info['price'] == 650

