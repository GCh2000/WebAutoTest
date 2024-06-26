from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com/")
# 绝对路径
# driver.find_element(By.XPATH, "/html/body/div/div/div[3]/a").click()
# 根据ID定位
# driver.find_element(By.XPATH, "//input[@id='kw']").send_keys('selenium')
# 根据class定位
# driver.find_element(By.XPATH, "//input[@class='s_ipt']").send_keys('selenium')
# 根据name定位
# driver.find_element(By.XPATH, "//input[@name='wd']").send_keys('selenium')
# 多个属性组合定位
# driver.find_element(By.XPATH, "//input[@name='wd' and @class='s_ipt' and @autocomplete='off']").send_keys('selenium')
# 多组数据使用下标定位
# driver.find_element(By.XPATH, "//div[@id='s-top-left']/a[4]").click()
# 通过子元素找父元素
# driver.find_element(By.XPATH, "//div[@id='s-top-left']/../div[3]").click()
# 根据span文本内容定位
driver.find_element(By.XPATH, "//span[text() = '坚定守护中华民族共同家园' ]").click()
sleep(3)
driver.close()