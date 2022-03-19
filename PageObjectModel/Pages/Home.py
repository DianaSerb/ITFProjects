from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class HomePage(Base):
    AUTOCOMPLETE = (By.LINK_TEXT, "Autocomplete")
    BUTTONS = (By.LINK_TEXT, "Buttons")
    CHECKBOX = (By.LINK_TEXT, "Checkbox")
    DATE = (By.LINK_TEXT, "Datepicker")
    DRAG = (By.LINK_TEXT, "Drag and Drop")
    DROPDOWN = (By.LINK_TEXT, "Dropdown")
    ENABLED = (By.LINK_TEXT, "Enabled and disbled elements")
    FILE = (By.LINK_TEXT, "File upload")
    PRESS = (By.LINK_TEXT, "Key and Mouse Press")
    MODAL = (By.LINK_TEXT, "Modal")
    SCROLL = (By.LINK_TEXT, "Page Scroll")
    RADIO = (By.LINK_TEXT, "Radio Button")
    SWITCH = (By.LINK_TEXT, "Switch window")
    FORUM = (By.LINK_TEXT, "Complete Web Forum")

    def click_on_autocomplete(self):
        print("We'll go to page autocomplete.")
        self._driver.find_element(*self.AUTOCOMPLETE).click()  # *=unpacking

    def click_on_checkbox(self):
        print("We'll go to page checkbox.")
        self._driver.find_element(*self.CHECKBOX).click()  # *=unpacking

    def click_on_buttons(self):
        self._driver.find_element(*self.BUTTONS).click()

    def click_on_date(self):
        self._driver.find_element(*self.DATE).click()

    def click_on_drag(self):
        self._driver.find_element(*self.DRAG).click()

    def click_on_dropdown(self):
        self._driver.find_element(*self.DROPDOWN).click()

    def click_on_enabled(self):
        self._driver.find_element(*self.ENABLED).click()

    def click_on_file(self):
        self._driver.find_element(*self.FILE).click()

    def click_on_press(self):
        self.driver.find_element(*self.PRESS).click()

    def click_on_modal(self):
        self.driver.find_element(*self.MODAL).click()

    def click_on_scroll(self):
        self.driver.find_element(*self.SCROLL).click()

    def click_on_radio(self):
        self.driver.find_element(*self.RADIO).click()

    def click_on_switch(self):
        self.driver.find_element(*self.SWITCH).click()

    def click_on_forum(self):
        self.driver.find_element(*self.FORUM).click()
