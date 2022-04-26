import time


from .BlazeApp import BasePage
from .Locators import BlazeLocators as BL


class BlazeHelpers(BasePage):
    def sign_up(self, username, password):
        self.go_home_page()
        self.go_home_page()
        self.find_element(BL.SIGN_UP_BUTTON).click()
        self.find_element(BL.SIGN_UP_LOGIN).send_keys(username)
        self.find_element(BL.SIGN_UP_PASS).send_keys(password)
        self.find_element(BL.SIGN_UP_CONFIRM).click()
        time.sleep(4)
        self.accept_alert()
        time.sleep(2)

    def sign_in(self, username, password):
        self.go_home_page()
        self.find_element(BL.SIGN_IN_BUTTON).click()
        self.find_element(BL.SIGN_IN_USERNAME).send_keys(username)
        self.find_element(BL.SIGN_IN_PASS).send_keys(password)
        self.find_element(BL.SIGN_IN_CONFIRM_BUTTON).click()
        time.sleep(2)

    def add_to_cart_items(self):
        self.find_element(BL.NEXUS_6).click()
        self.find_element(BL.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        self.find_element(BL.HOME).click()
        self.find_element(BL.LAPTOP_CAT).click()
        self.find_element(BL.MACBOOK_PRO).click()
        self.find_element(BL.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        self.find_element(BL.HOME).click()
        self.find_element(BL.MONITOR_CAT).click()
        self.find_element(BL.APPLE_MONITOR).click()
        self.find_element(BL.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)

    def list_of_items_in_cart(self):
        self.find_element(BL.CART).click()
        time.sleep(2)
        cart_list = [
            self.find_element(BL.ITEM_1).text,
            self.find_element(BL.ITEM_2).text,
            self.find_element(BL.ITEM_3).text
        ]
        return cart_list

    def total_sum(self):
        price_list = [
            self.find_element(BL.PRICE_1).text,
            self.find_element(BL.PRICE_2).text,
            self.find_element(BL.PRICE_3).text
        ]
        total_sum = 0
        for i in price_list:
            s = int(i)
            total_sum += s
        return total_sum

    def place_an_order_get_total_amount(self):
        self.find_element(BL.PLACE_ORDER_BUTTON).click()
        self.find_element(BL.ORDER_NAME).send_keys('Name')
        self.find_element(BL.ORDER_CARD).send_keys('444555')
        self.find_element(BL.PURCHASE_BUTTON).click()
        time.sleep(1)
        self.switch_to_active_element()
        order_info = self.find_element(BL.ORDER_INFO).text
        order_sum = int(str(order_info.splitlines()[1]).replace("Amount: ", " ").replace(" USD", " ").strip())
        return order_sum
