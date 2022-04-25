from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.demoblaze.com/"
        #self.url = "https://demoblaze.com/"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_home_page(self):
        return self.driver.get(self.base_url)

    def accept_alert(self):
        return self.driver.switch_to.alert.accept()

    def switch_to_active_element(self):
        return self.driver.switch_to.active_element