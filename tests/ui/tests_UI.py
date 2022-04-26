from tests.logger.logger import get_logger
from tests.ui.page_objects.LoginPage import LoginPage
from tests.ui.page_objects.CartPage import CartPage
from tests.ui.helpers.ui_helper import save_username_to_file, unique_user

"""
PATH_TO_FILE should be specified on each env
"""
USER = unique_user()
PASSWORD = '111'
PATH_TO_FILE = 'E:/dd/ViaTr/tests/user.json'
save_username_to_file(USER, PATH_TO_FILE)

log = get_logger()


def test_sign_up_and_by_3_items(browser):
    log.info("\nSign up and log in with new user - %s", USER)
    LoginPage(browser).sign_up(username=USER, password=PASSWORD)
    LoginPage(browser).sign_in(username=USER, password=PASSWORD)
    log.info("Add 3 items to cart")
    CartPage(browser).add_to_cart_items()
    list_of_items_in_cart = CartPage(browser).list_of_items_in_cart()
    log.info("Checking that all added items are in cart")
    log.info("Checking that all added items are in cart")
    assert "Nexus 6" and "MacBook Pro" and "Apple monitor 24" in list_of_items_in_cart
    log.info("Asserting total sum in cart is correct")
    assert CartPage(browser).total_sum() == 2150
    log.info("Asserting sum order is correct")
    assert CartPage(browser).place_an_order_get_total_amount() == 2150
