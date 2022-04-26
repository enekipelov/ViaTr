from selenium.webdriver.common.by import By


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