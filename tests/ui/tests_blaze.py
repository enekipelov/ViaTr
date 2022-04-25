import time
from tests.ui.BlazePages import BlazeHelpers


def test_sign_in(browser):
    blazedemo = BlazeHelpers(browser)
    blazedemo.sign_up()
    time.sleep(2)
    blazedemo.add_to_cart_items()
    time.sleep(2)
    list_of_items_in_cart =  blazedemo.list_of_items_in_cart()
    assert "Nexus 6" and "MacBook Pro" and "Apple monitor 24" in list_of_items_in_cart
    assert blazedemo.total_sum() == 2150
    assert blazedemo.place_an_order_get_total_amount() == 2150