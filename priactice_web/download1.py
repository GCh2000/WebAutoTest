import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path = "D:/Python projects/WebAutoTest/file/LATEST_RELEASE"
if os.path.exists(path):
    os.remove(path)
chromeOptions = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 0,
    'download.default_directory': 'D:/desktop'}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chromeOptions)
driver.maximize_window()
driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver/")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/table/tbody/tr[156]/td[2]/a').click()
time.sleep(10)
driver.close()
