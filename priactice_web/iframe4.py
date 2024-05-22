import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/iframesTest.htm")
driver.find_element(By.ID, "checkRecord").clear()
driver.find_element(By.ID, "checkRecord").send_keys("666")
time.sleep(3)
# 通过元素找到
ele = driver.find_element(By.CSS_SELECTOR, "body > iframe")
# 进入iframe
driver.switch_to.frame(ele)
# 退出iframe，切换到上一级
# driver.switch_to.parent_frame()
# 切换到主界面
driver.switch_to.default_content()
driver.find_element(By.ID, "checkRecord").clear()
driver.find_element(By.ID, "checkRecord").send_keys("777")
time.sleep(3)
driver.close()
