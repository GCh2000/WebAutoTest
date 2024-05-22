import time

import pytest
from selenium.webdriver.common.by import By

from utils.read import read_yaml


# @pytest.mark.parametrize("key", ["接口自动化", "UI自动化", "性能测试"])
@pytest.mark.parametrize("key", read_yaml()['skill'])
def test_baidu(driver, key):
    driver.get("https://www.baidu.com/")
    driver.find_element(By.ID, 'kw').send_keys(key)
    driver.find_element(By.ID, 'su').click()
    time.sleep(1)
