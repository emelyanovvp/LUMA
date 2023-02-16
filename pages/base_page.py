import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
