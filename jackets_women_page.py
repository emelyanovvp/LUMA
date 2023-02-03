from .base_page import BasePage
from .olivia_jacket_page import OliviaJacketPage
from selenium.webdriver.common.by import By
from .locators import JacketsWomenLocators
from .cart_page import CartPage
from selenium.webdriver.common.action_chains import ActionChains
import time
class JacketsWomenPage(BasePage):
    def should_be_women_page(self):
        self.should_be_style_link()
        self.should_be_price_link()
        self.should_be_size_link()

    def customer_can_click_and_go_to_olivia_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA).click()
        return OliviaJacketPage(driver=self.driver, url=self.driver.current_url)

    def customer_can_choose_size_M_and_colour_purple_then_add_product_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR,"#option-label-size-143-item-168").click()
        self.driver.find_element(By.CSS_SELECTOR,"#option-label-color-93-item-57").click()
        self.driver.find_element(By.CSS_SELECTOR,"button.tocart>span").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,".showcart").click()
        time.sleep(5)
        show_cart = self.driver.find_element(By.CSS_SELECTOR,".viewcart>span").click()
        return CartPage(driver=self.driver, url=self.driver.current_url)


