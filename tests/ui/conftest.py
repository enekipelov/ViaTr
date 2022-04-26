import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", choices=["chrome", "firefox", "ie"], help="Choose browser")
    parser.addoption("--baseurl", default="https://demoblaze.com/")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")

    driver = None
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = False
        driver = webdriver.Firefox(executable_path=r'E:\drivers\geckodriver.exe')
        driver.maximize_window()
    elif browser == "ie":
        options = webdriver.IeOptions()
        options.headless = True
        driver = webdriver.Ie(options=options)
        driver.maximize_window()

    yield driver
    driver.quit()
