from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class Buttons(Base):
    PRIMARY = (By.XPATH, "/html/body/div/form/div[1]/div/div/button[1]")
    SUCCESS = (By.XPATH, "/html/body/div/form/div[1]/div/div/button[2]")
    MIDDLE = (By.XPATH, "/html/body/div/form/div[2]/div/div/div/button[2]")
    DROPDOWN = (By.ID, "btnGroupDrop1")
    DRLINK2 = (By.XPATH, "/html/body/div/form/div[3]/div/div/div/div/div/a[2]")

    def click_primary(self):
        self._driver.find_element(*self.PRIMARY).click()

    def click_success(self):
        self._driver.find_element(*self.SUCCESS).click()

    def click_middle(self):
        self._driver.find_element(*self.MIDDLE).click()

    def click_dropdown(self):
        self._driver.find_element(*self.DROPDOWN).click()

    def click_drlink2(self):
        self._driver.find_element(*self.DRLINK2).click()

