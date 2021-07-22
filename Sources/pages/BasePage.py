from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import TestData


class BasePage:
    """This is Base page with common actions and utilities."""

    def __init__(self, browser):
        self.driver = browser
        self.open_page()

    def open_page(self):
        try:
            self.driver.get(TestData.BASE_URL)
            print("Application URL: " + TestData.BASE_URL + " is successfully opened")
        except Exception as e:
            print("open_page exception: " + e)
            assert False

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
