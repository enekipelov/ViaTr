from selenium.webdriver.common.by import By


class Login:
    SIGN_IN_BUTTON = (By.ID, "login2")
    SIGN_IN_USERNAME = (By.ID, 'loginusername')
    SIGN_IN_PASS = (By.ID, 'loginpassword')
    SIGN_IN_CONFIRM_BUTTON = (By.XPATH, '//button[@onclick="logIn()"]')

    SIGN_UP_BUTTON = (By.ID, 'signin2')
    SIGN_UP_LOGIN = (By.ID, 'sign-username')
    SIGN_UP_PASS = (By.ID, 'sign-password')
    SIGN_UP_CONFIRM = (By.XPATH, '//button[text() = "Sign up"]')
