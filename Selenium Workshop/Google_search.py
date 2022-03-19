import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

time.sleep(2)
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)
SEARCH = (By.NAME, "q")
DEACORD = (By.ID, "L2AGLb")
driver.find_element(*DEACORD).click()
time.sleep(2)
search_bar = driver.find_element(*SEARCH)
time.sleep(2)
search_bar.send_keys("pizza")
time.sleep(2)
search_bar.submit()
time.sleep(4)

driver.quit()

#TODO verificam daca in rezultatele  cautarii se regasesc rez cu cuvantul cautat
#integrare unit test ->assertIn
#functie->parametru (cautari diverse)-> fisier JSON
