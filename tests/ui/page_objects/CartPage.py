import time

from tests.ui.page_objects.BasePage import BasePage
from tests.ui.locators.Cart import Cart


class CartPage(BasePage):
    def add_to_cart_items(self):
        self.find_element(Cart.NEXUS_6).click()
        self.find_element(Cart.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        self.find_element(Cart.HOME).click()
        self.find_element(Cart.LAPTOP_CAT).click()
        self.find_element(Cart.MACBOOK_PRO).click()
        self.find_element(Cart.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        self.find_element(Cart.HOME).click()
        self.find_element(Cart.MONITOR_CAT).click()
        self.find_element(Cart.APPLE_MONITOR).click()
        self.find_element(Cart.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)

    def list_of_items_in_cart(self):
        self.find_element(Cart.CART).click()
        time.sleep(2)
        cart_list = [
            self.find_element(Cart.ITEM_1).text,
            self.find_element(Cart.ITEM_2).text,
            self.find_element(Cart.ITEM_3).text
        ]
        return cart_list

    def total_sum(self):
        price_list = [
            self.find_element(Cart.PRICE_1).text,
            self.find_element(Cart.PRICE_2).text,
            self.find_element(Cart.PRICE_3).text
        ]
        total_sum = 0
        for i in price_list:
            s = int(i)
            total_sum += s
        return total_sum

    def place_an_order_get_total_amount(self):
        self.find_element(Cart.PLACE_ORDER_BUTTON).click()
        self.find_element(Cart.ORDER_NAME).send_keys('Name')
        self.find_element(Cart.ORDER_CARD).send_keys('444555')
        self.find_element(Cart.PURCHASE_BUTTON).click()
        time.sleep(1)
        self.switch_to_active_element()
        order_info = self.find_element(Cart.ORDER_INFO).text
        order_sum = int(str(order_info.splitlines()[1]).replace("Amount: ", " ").replace(" USD", " ").strip())
        return order_sum
