from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def check_name_size_and_color_on_cart_page(self):
        name = self.driver.find_element(By.CSS_SELECTOR,"strong.product-item-name>a")
        size = self.driver.find_element(By.CSS_SELECTOR,"dd.cf-tweet-this")
        color = self.driver.find_element(By.CSS_SELECTOR,"dd.cf-tt-enabled")

