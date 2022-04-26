import time

from selenium.webdriver.common.by import By

from .BlazeApp import BasePage


class BlazeLocators:
    SIGN_IN_BUTTON = (By.ID, "login2")
    SIGN_IN_USERNAME = (By.ID, 'loginusername')
    SIGN_IN_PASS = (By.ID, 'loginpassword')
    SIGN_IN_CONFIRM_BUTTON = (By.XPATH, '//button[@onclick="logIn()"]')

    PHONES_CAT = (By.XPATH, '//a[@onclick="byCat(\'phone\')"]')
    LAPTOP_CAT = (By.XPATH, '//a[@onclick="byCat(\'notebook\')"]')
    MONITOR_CAT = (By.XPATH, '//a[@onclick="byCat(\'monitor\')"]')

    NEXUS_6 = (By.XPATH, '//a[text()="Nexus 6"]')
    MACBOOK_PRO = (By.XPATH, '//a[text()="MacBook Pro"]')
    APPLE_MONITOR = (By.XPATH, '//a[text()="Apple monitor 24"]')
    HOME = (By.XPATH, '//li/a[@href="index.html"]')

    CART = (By.XPATH, '//a[text()="Cart"]')
    ADD_TO_CART = (By.XPATH, '//a[text()="Add to cart"]')
    ITEM_1 = (By.XPATH, '//*[@id="tbodyid"]/tr[1]/td[2]')
    ITEM_2 = (By.XPATH, '//*[@id="tbodyid"]/tr[2]/td[2]')
    ITEM_3 = (By.XPATH, '//*[@id="tbodyid"]/tr[3]/td[2]')
    PRICE_1 = (By.XPATH, '//*[@id="tbodyid"]/tr[1]/td[3]')
    PRICE_2 = (By.XPATH, '//*[@id="tbodyid"]/tr[2]/td[3]')
    PRICE_3 = (By.XPATH, '//*[@id="tbodyid"]/tr[3]/td[3]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Place Order"]')
    ORDER_NAME = (By.ID, 'name')
    ORDER_CARD = (By.ID, 'card')
    PURCHASE_BUTTON = (By.XPATH, '//button[text()=\'Purchase\']')
    ORDER_INFO = (By.XPATH, '//*[text()[contains(.,\'USD\')]]')

    SIGN_UP_BUTTON = (By.ID, 'signin2')
    SIGN_UP_LOGIN = (By.ID, 'sign-username')
    SIGN_UP_PASS = (By.ID, 'sign-password')
    SIGN_UP_CONFIRM = (By.XPATH, '//button[text() = "Sign up"]')


class BlazeHelpers(BasePage):
    def sign_up(self, username, password):
        self.go_home_page()
        self.go_home_page()
        self.find_element(BlazeLocators.SIGN_UP_BUTTON).click()
        self.find_element(BlazeLocators.SIGN_UP_LOGIN).send_keys(username)
        self.find_element(BlazeLocators.SIGN_UP_PASS).send_keys(password)
        self.find_element(BlazeLocators.SIGN_UP_CONFIRM).click()
        time.sleep(4)
        self.accept_alert()

    def sign_in(self, username, password):
        self.go_home_page()
        self.find_element(BlazeLocators.SIGN_IN_BUTTON).click()
        self.find_element(BlazeLocators.SIGN_IN_USERNAME).send_keys(username)
        self.find_element(BlazeLocators.SIGN_IN_PASS).send_keys(password)
        self.find_element(BlazeLocators.SIGN_IN_CONFIRM_BUTTON).click()

    def add_to_cart_items(self):
        self.find_element(BlazeLocators.NEXUS_6).click()
        self.find_element(BlazeLocators.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        self.find_element(BlazeLocators.HOME).click()
        self.find_element(BlazeLocators.LAPTOP_CAT).click()
        self.find_element(BlazeLocators.MACBOOK_PRO).click()
        self.find_element(BlazeLocators.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()
        self.find_element(BlazeLocators.HOME).click()
        self.find_element(BlazeLocators.MONITOR_CAT).click()
        self.find_element(BlazeLocators.APPLE_MONITOR).click()
        self.find_element(BlazeLocators.ADD_TO_CART).click()
        time.sleep(2)
        self.accept_alert()

    def list_of_items_in_cart(self):
        self.find_element(BlazeLocators.CART).click()
        time.sleep(2)
        cart_list = [
            self.find_element(BlazeLocators.ITEM_1).text,
            self.find_element(BlazeLocators.ITEM_2).text,
            self.find_element(BlazeLocators.ITEM_3).text
        ]
        return cart_list

    def total_sum(self):
        price_list = [
            self.find_element(BlazeLocators.PRICE_1).text,
            self.find_element(BlazeLocators.PRICE_2).text,
            self.find_element(BlazeLocators.PRICE_3).text
        ]
        total_sum = 0
        for i in price_list:
            s = int(i)
            total_sum += s
        return total_sum

    def place_an_order_get_total_amount(self):
        self.find_element(BlazeLocators.PLACE_ORDER_BUTTON).click()
        self.find_element(BlazeLocators.ORDER_NAME).send_keys('Name')
        self.find_element(BlazeLocators.ORDER_CARD).send_keys('444555')
        self.find_element(BlazeLocators.PURCHASE_BUTTON).click()
        time.sleep(1)
        self.switch_to_active_element()
        order_info = self.find_element(BlazeLocators.ORDER_INFO).text
        order_sum = int(str(order_info.splitlines()[1]).replace("Amount: ", " ").replace(" USD", " ").strip())
        return order_sum
