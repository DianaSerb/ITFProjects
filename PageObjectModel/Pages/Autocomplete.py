from PageObjectModel.Pages.Base import Base
from selenium.webdriver.common.by import By


class Autocomplete(Base):
    ADDRESS = (By.ID, "autocomplete")
    SADRESS = (By.ID, "street_number")  # street address field
    SADRESS2 = (By.ID, "route")
    CITY = (By.ID, "locality")
    STATE = (By.ID, "administrative_area_level_1")
    ZIP = (By.ID, "postal_code")
    COUNTRY = (By.ID, "country")

    def enter_addr(self, address):
        self._driver.find_element(*self.ADDRESS).click()
        self._driver.find_element(*self.ADDRESS).send_keys(address)

    def enter_str1(self, street1):
        self._driver.find_element(*self.SADRESS).send_keys(street1)

    def enter_str2(self, street2):
        self._driver.find_element(*self.SADRESS2).send_keys(street2)

    def enter_city(self, city):
        self._driver.find_element(*self.CITY).send_keys(city)

    def enter_state(self, state):
        self._driver.find_element(*self.STATE).send_keys(state)

    def enter_zip(self, zipcode):
        self._driver.find_element(*self.ZIP).send_keys(zipcode)

    def enter_country(self, country):
        self._driver.find_element(*self.COUNTRY).send_keys(country)

    def check_address_result(self):
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "body > div.pac-container.hdpi > div > div:nth-child(2) > span").text
