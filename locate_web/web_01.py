import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 定义一个driver的变量，用来接受实例化后的浏览器
driver = webdriver.Chrome()
# 使用get方法，访问网址
driver.get("https://www.bilibili.com")
# 1.找到输入框位置，发送软件测试老白
driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys("软件测试老白")
# 2.找到搜索框位置，点击搜索
driver.find_element(By.CLASS_NAME, 'nav-search-btn').click()
time.sleep(3)
driver.close()
