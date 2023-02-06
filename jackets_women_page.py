from .base_page import BasePage
from .olivia_jacket_page import OliviaJacketPage
from selenium.webdriver.common.by import By
from .locators import JacketsWomenLocators
from .locators import CartWindowLocators
from .cart_page import CartPage
from selenium.webdriver.common.action_chains import ActionChains
import time
class JacketsWomenPage(BasePage):

    def customer_can_click_and_go_to_olivia_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_NAME).click()
        return OliviaJacketPage(driver=self.driver, url=self.driver.current_url)

    def choose_size_and_colour_then_add_product_to_cart(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_SIZE).click()
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_COLOR).click()
        self.driver.find_element(*JacketsWomenLocators.BUTTON_ADD_TO_CART).click()
        time.sleep(10)

    def go_to_cart_window(self):
        self.driver.find_element(*JacketsWomenLocators.SHOW_BASKET_WINDOW).click()
        time.sleep(10)

    def go_to_cart_page_from_cart_window(self):
        show_cart = self.driver.find_element(*JacketsWomenLocators.VIEW_CART_PAGE).click()
        return CartPage(driver=self.driver, url=self.driver.current_url)

    def check_jacket_name_in_cart(self):
        name_element = self.driver.find_element(*CartWindowLocators.NAME)
        assert name_element.text == "Olivia 1/4 Zip Light Jacket", "Olivia name is not presented in cart"

    def check_quantity_of_jackets_in_cart(self):
        quantity_element = self.driver.find_element(*CartWindowLocators.Quantity)
        assert quantity_element.text == '1', "Quantity of jackets is not 1"

    def check_size_of_jacket(self):
        button_see_details = self.driver.find_element(*CartWindowLocators.SEE_DETAILS).click()
        size_element = self.driver.find_element(*CartWindowLocators.SIZE)
        assert size_element.text == "M", "Size M is not presented in cart"
    def check_color_of_jacket(self):
        button_see_details = self.driver.find_element(*CartWindowLocators.SEE_DETAILS).click()
        color_element = self.driver.find_element(*CartWindowLocators.COLOR)
        assert color_element.text == "Purple", "Color Purple is not presented in cart"


