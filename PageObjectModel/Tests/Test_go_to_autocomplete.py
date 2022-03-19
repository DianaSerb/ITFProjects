import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestGoToAuto(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome("C:/Users/serbd/Desktop/GitHub/ITFProjects/Resources/chromedriver.exe")
        self.driver.get("http://formy-project.herokuapp.com/")

    def test_autocomplete(self):
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Autocomplete").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "autocomplete").send_keys("Cluj-Napoca")
        time.sleep(2)
        result = self.driver.find_element(By.CSS_SELECTOR,
                                          "body > div.pac-container.hdpi > div > div:nth-child(2) > span")
        self.assertIn("Cluj-Napoca", result.text)  # assertIn verifica daca se regaseste in result
        # TODO completare form de adrese, terminat de mapat +teste

    def tearDown(self) -> None:
        self.driver.quit()


