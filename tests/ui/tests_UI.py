from tests.logger.logger import get_logger
from tests.ui.BlazePages import BlazeHelpers
from tests.ui.ui_helper import save_username_to_file, unique_user

USER = unique_user()
PASSWORD = '111'
# in PATH_TO_FILE stored username for login
PATH_TO_FILE = 'E:/dd/ViaTr/tests/user.json'
save_username_to_file(USER, PATH_TO_FILE)

log = get_logger()


def test_sign_up_and_by_3_items(browser):
    blazedemo = BlazeHelpers(browser)
    log.info("\nSign up and log in with new user - %s", USER)
    blazedemo.sign_up(username=USER, password=PASSWORD)
    blazedemo.sign_in(username=USER, password=PASSWORD)
    log.info("Add 3 items to cart")
    blazedemo.add_to_cart_items()
    list_of_items_in_cart = blazedemo.list_of_items_in_cart()
    log.info("Checking that all added items are in cart")
    log.info("Checking that all added items are in cart")
    assert "Nexus 6" and "MacBook Pro" and "Apple monitor 24" in list_of_items_in_cart
    log.info("Asserting total sum in cart is correct")
    assert blazedemo.total_sum() == 2150
    log.info("Asserting sum oreder is correct")
    assert blazedemo.place_an_order_get_total_amount() == 2150
