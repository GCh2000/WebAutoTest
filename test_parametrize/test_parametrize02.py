import time

import pytest
from selenium.webdriver.common.by import By

from utils.read import read_yaml


# @pytest.mark.parametrize("data", read_yaml()['userinfos'])  # 这里只能用一个变量接收，因为是一个字典数组，直接用2个变量接收会有问题；用一个接收则得到的是第一个字典
@pytest.mark.parametrize("username,password", read_yaml()['userinfo_list'])  # 如果是列表形式就是可以的
def test_login(driver, username, password):
    driver.get("http://sellshop.5istudy.online/sell/user/login_page")
    # driver.find_element(By.ID, 'username').send_keys(data['username']) # 对应第一种方式
    driver.find_element(By.ID, 'username').send_keys(username)
    # driver.find_element(By.ID, 'password').send_keys(data['password']) # 对应第二种方式
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
    if username == 'admin':
        text = driver.find_element(By.CSS_SELECTOR,"body > div > div > div > div > strong").text
        assert text == '用户不存在'
    time.sleep(2)

