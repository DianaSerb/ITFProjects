import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Autocomplete import Autocomplete
from PageObjectModel.Pages.Home import HomePage


class TestGoToAuto2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome("C:/Users/serbd/Desktop/GitHub/ITFProjects/Resources/chromedriver.exe")
        self.driver.get("http://formy-project.herokuapp.com/")

    def test_autocomplete(self):
        home = HomePage(self.driver)
        autocomplete = Autocomplete(self.driver)
        time.sleep(1)
        home.click_on_autocomplete()
        time.sleep(2)
        autocomplete.enter_addr("Bucharest")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "dismissButton").click()
        time.sleep(1)
        # TODO completare form de adrese
        autocomplete.enter_str1("Bulevardul Magheru 3")
        time.sleep(2)
        autocomplete.enter_str2("bl 2, etaj 1")
        time.sleep(2)
        autocomplete.enter_city("Bucuresti")
        time.sleep(2)
        self.assertIn("Bucharest", autocomplete.check_address_result())

    def tearDown(self) -> None:
        self.driver.quit()
