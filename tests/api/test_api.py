from . import api
from .api_helper import get_username_from_file
from tests.logger.logger import get_logger

API_URL = 'https://api.demoblaze.com/'
PATH_TO_FILE = 'E:/dd/ViaTr/tests/user.json'
ITEM_ID = '3'
LOGIN = get_username_from_file(PATH_TO_FILE)
PASSWORD = '111'

log = get_logger()

def test_add_item_to_cart():
    log.info('\n')
    log.info("\nLogin to Demoblaze.com using login created during UI tests, login - %s",LOGIN)
    token = api.login_api(api_url=API_URL, username=LOGIN, password=PASSWORD)
    log.info("Addin to cart test item, id = %s",ITEM_ID)
    api.add_to_cart(api_url=API_URL, token=token, product_id=ITEM_ID)
    log.info("Checking item in cart")
    items_in_cart = api.view_cart(api_url=API_URL, token=token)
    log.info('Asserting number of items in the cart and items id')
    assert items_in_cart['Items'][0]["prod_id"] == ITEM_ID
    assert len(items_in_cart['Items']) == 1
    log.info("Asserting item info is coorect")
    item_info = api.view_item_info(api_url=API_URL, product_id=ITEM_ID)
    assert item_info['title'] == 'Nexus 6'
    assert item_info['price'] == 650
