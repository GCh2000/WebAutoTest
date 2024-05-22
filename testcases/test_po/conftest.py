import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
