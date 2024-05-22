import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/alertTest.htm")
driver.find_element(By.NAME, 'b1').click()
# 使用alert.text获取弹框的文字
print(driver.switch_to.alert.text)
# 点击确定
driver.switch_to.alert.accept()
time.sleep(3)
driver.close()
