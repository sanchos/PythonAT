from config.config import TestData
from pages.LoginPage import LoginPage


def test_login_button_visible(browser):
    loginPage = LoginPage(browser)
    flag = loginPage.is_login_button_exist()
    assert flag


def test_login(browser):
    loginPage = LoginPage(browser)
    loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)


def test_testing_data(create_test_data):
    print(create_test_data)
