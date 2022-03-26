import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestBasicAuth(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()

    def test_basic_auth(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(3) > a").click()
        user = "admin"
        password = "admin"
        time.sleep(2)
        self.driver.get("https://" + user + ":" + password + "@the-internet.herokuapp.com/basic_auth")
        time.sleep(2)
        message = self.driver.find_element(By.CSS_SELECTOR, "#content > div > p").text
        print(message)
        time.sleep(2)
        self.driver.back()
        self.driver.back()

    def tearDown(self) -> None:
        self.driver.quit()
