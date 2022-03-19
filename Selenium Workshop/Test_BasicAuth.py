import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
driver.maximize_window()

AUTHBUTTON = (By.CSS_SELECTOR, "#content > ul > li:nth-child(3) > a")
MESSAGE = (By.CSS_SELECTOR, "#content > div > p")
user = "admin"
password = "admin"

driver.find_element(*AUTHBUTTON).click()

time.sleep(3)

driver.get("https://" + user + ":" + password + "@the-internet.herokuapp.com/basic_auth")

message = driver.find_element(*MESSAGE).text
print(message)

time.sleep(2)
driver.back()
driver.back()
time.sleep(2)

driver.quit()

#TODO migrare unittest
