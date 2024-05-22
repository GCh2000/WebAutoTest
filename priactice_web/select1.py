import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/selectTest.htm")
time.sleep(1)
select = Select(driver.find_element(By.ID, 's1'))
# select.select_by_index(1)
# 根据option的value进行选择
# select.select_by_value("51")
# 根据实际看到的内容进行选择
select.select_by_visible_text("Cell Phone")
time.sleep(3)
driver.close()
