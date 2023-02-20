import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .locators import JacketsWomenLocators
class BasePage():
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)
    def open(self):
        self.driver.get(self.url)
    def is_element_clickable(self,how,what,timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((how,what)))
        except TimeoutException:
            return False
        return True

    def is_expected_element_presented(self,how,what):
       element = self.driver.find_element(how,what)
       return element.text
