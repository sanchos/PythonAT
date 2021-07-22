from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure
from allure_commons.types import AttachmentType


class LoginPage(BasePage):
    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")

    """Page actions"""
    @allure.step('is_login_button_exist')
    @allure.severity('blocker')
    def is_login_button_exist(self):
        with allure.step('Screenshot:'):
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        return self.is_visible(self.LOGIN_BUTTON)

    @allure.step('Login to application')
    @allure.severity('blocker')
    def do_login(self, username, password):
        with allure.step('Screenshot:'):
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        self.type_username(username)
        self.type_password(password)
        self.do_click(self.LOGIN_BUTTON)

    @allure.step('Type username')
    def type_username(self, username):
        self.do_send_keys(self.USERNAME, username)

    @allure.step('Type password')
    def type_password(self, password):
        self.do_send_keys(self.PASSWORD, password)

