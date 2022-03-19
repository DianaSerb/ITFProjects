import unittest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Buttons import Buttons
from PageObjectModel.Pages.Home import HomePage


class TestButtons(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome("C:/Users/serbd/Desktop/GitHub/ITFProjects/Resources/chromedriver.exe")
        self.driver.get("http://formy-project.herokuapp.com/")

    def test_buttons(self):
        home = HomePage(self.driver)
        buttons = Buttons(self.driver)
        time.sleep(1)
        home.click_on_buttons()
        time.sleep(2)
        buttons.click_primary()
        time.sleep(1)
        buttons.click_success()
        time.sleep(1)
        buttons.click_middle()
        time.sleep(1)
        buttons.click_dropdown()
        time.sleep(1)
        buttons.click_drlink2()
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()
