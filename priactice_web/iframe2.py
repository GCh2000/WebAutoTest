import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# 打开本地的html文件，前面要加file://
driver.get("file://D:\Python projects\WebAutoTest\html\iframe_test.html")
driver.find_element(By.ID, "checkRecord").clear()
driver.find_element(By.ID, "checkRecord").send_keys("666")
time.sleep(3)
# 用id
# driver.switch_to.frame("iframe_id")
# driver.find_element(By.XPATH, "//span[text()='番剧']").click()
# 用id
driver.switch_to.frame("iframe_name")
driver.find_element(By.XPATH, "//span[text()='番剧']").click()
time.sleep(3)
driver.close()
