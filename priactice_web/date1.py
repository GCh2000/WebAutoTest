import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/date-picker")
driver.find_element(By.XPATH, "//input[@class='ivu-input ivu-input-default ivu-input-with-suffix']").send_keys('2024-04-12')
driver.find_elements(By.XPATH, "//input[@class='ivu-input ivu-input-default ivu-input-with-suffix']")[1].send_keys('2024-04-12 - 2024-05-02')
time.sleep(3)
driver.close()