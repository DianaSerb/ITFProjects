import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestMultiTab(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://the-internet.herokuapp.com/windows")

    def test(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > div > a").click()
        first_tab = self.driver.window_handles[0]
        second_tab = self.driver.window_handles[1]
        time.sleep(2)

        i = 0

        while i < 15:
            self.driver.switch_to.window(first_tab)
            self.driver.switch_to.window(second_tab)
            i += 1

    def tearDown(self) -> None:
        self.driver.quit()
