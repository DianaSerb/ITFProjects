import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Checkbox import Checkbox
from PageObjectModel.Pages.Home import HomePage


def test_checkbox():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://formy-project.herokuapp.com/")
    time.sleep(2)
    home = HomePage(driver)
    checkbox = Checkbox(driver)
    home.click_on_checkbox()
    time.sleep(2)
    checkbox.select_checkbox1()
    time.sleep(2)
    checkbox.select_checkbox2()
    time.sleep(2)
    checkbox.select_checkbox3()
    time.sleep(2)
    checkbox.select_checkbox1()
    time.sleep(2)
    checkbox.select_checkbox2()
    time.sleep(2)
    checkbox.select_checkbox3()
    driver.quit()

if __name__ == '__main__':
    test_checkbox()
