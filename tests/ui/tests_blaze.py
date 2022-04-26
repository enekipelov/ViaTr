import time

from tests.ui.BlazePages import BlazeHelpers
from tests.ui.ui_helper import save_username_to_file, unique_user

USER = unique_user()
PASSWORD = '111'
# in PATH_TO_FILE stored username for login
PATH_TO_FILE = 'E:/dd/ViaTr/tests/user.json'
save_username_to_file(USER, PATH_TO_FILE)


def test_sign_up_and_by_3_items(browser):
    blazedemo = BlazeHelpers(browser)
    blazedemo.sign_up(username=USER, password=PASSWORD)
    time.sleep(2)
    blazedemo.sign_in(username=USER, password=PASSWORD)
    time.sleep(2)
    blazedemo.add_to_cart_items()
    time.sleep(2)
    list_of_items_in_cart = blazedemo.list_of_items_in_cart()
    assert "Nexus 6" and "MacBook Pro" and "Apple monitor 24" in list_of_items_in_cart
    assert blazedemo.total_sum() == 2150
    assert blazedemo.place_an_order_get_total_amount() == 2150
