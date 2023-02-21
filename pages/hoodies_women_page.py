from .base_page import BasePage
from .locators import BasePageLocators
from .locators import WomenPageLocators
from .locators import CartWindowLocators
from .locators import SuccessfulMessageLOCATORS
from .cart_page import CartPage
import time

class HoodiesWomenPage(BasePage):
    def customer_can_go_to_olivia_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_NAME).click()
        return OliviaJacketPage(driver=self.driver, url=self.driver.current_url)