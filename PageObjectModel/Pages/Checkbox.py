from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class Checkbox(Base):
    CHK1 = (By.ID, "checkbox-1")
    CHK2 = (By.ID, "checkbox-2")
    CHK3 = (By.ID, "checkbox-3")

    def select_checkbox1(self):
        self._driver.find_element(*self.CHK1).click()

    def select_checkbox2(self):
        self._driver.find_element(*self.CHK2).click()

    def select_checkbox3(self):
        self._driver.find_element(*self.CHK3).click()
