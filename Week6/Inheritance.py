class Base:
    def __init__(self, driver):
        self._browser = driver

    def open_browser(self, url):
        print(f"Open {self._browser}. Browser for {url}")

    @staticmethod
    def quit_browser():
        print("Browser closed")


class Child(Base):
    def setup(self):
        print("Set your test environment")
        self.open_browser("https://www.youtube.com")

    @staticmethod
    def run_steps():
        print("Steps to be added later on.")

    def tear_down(self):
        print("Quit test")
        self.quit_browser()


class FirstTest(Child):
    def run_steps(self):
        print("Step 1: ")
        print("Step 2: ")
        print("Step 3: ")


class SecondTest(Child):
    def run_steps(self):
        print("Enter the invalid credentials.")


if __name__ == '__main__':  # se ruleaza doar in acest fisier
    chrome = Base("chrome_driver")  # obiect
    chrome.open_browser("https://www.anaf.ro")  # apelare metoda
    chrome.quit_browser()

    child = Child("Firefox")
    child.setup()
    child.run_steps()
    child.tear_down()

    test1 = FirstTest("Safari")
    test2 = SecondTest("Edge")

    test1.run_steps()
    test2.run_steps()

    print(SecondTest.mro())
