import time

from tests.ui.page_objects.BasePage import BasePage
from tests.ui.locators.Login import Login


class LoginPage(BasePage):
    def sign_up(self, username, password):
        self.go_home_page()
        self.go_home_page()
        self.find_element(Login.SIGN_UP_BUTTON).click()
        self.find_element(Login.SIGN_UP_LOGIN).send_keys(username)
        self.find_element(Login.SIGN_UP_PASS).send_keys(password)
        self.find_element(Login.SIGN_UP_CONFIRM).click()
        time.sleep(4)
        self.accept_alert()
        time.sleep(2)

    def sign_in(self, username, password):
        self.go_home_page()
        self.find_element(Login.SIGN_IN_BUTTON).click()
        self.find_element(Login.SIGN_IN_USERNAME).send_keys(username)
        self.find_element(Login.SIGN_IN_PASS).send_keys(password)
        self.find_element(Login.SIGN_IN_CONFIRM_BUTTON).click()
        time.sleep(4)
