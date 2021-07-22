import pytest
from selenium import webdriver
from config.config import TestData
from data.data_generation import DataGen


@pytest.fixture()
def browser():
    browser_type = TestData.BROWSER_TYPE
    if browser_type == 'local':
        driver = webdriver.Chrome()
    elif browser_type == 'cloud':
        capabilities = {'browserName': 'chrome', 'enableVNC': True}
        driver = webdriver.Remote(
            command_executor=TestData.SELENIDE_SERVER,
            desired_capabilities=capabilities)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def create_test_data():
    data = DataGen.data_gen()
    yield data

