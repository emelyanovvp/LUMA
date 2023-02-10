from .base_page import BasePage
from .olivia_jacket_page import OliviaJacketPage
from .juno_jacket_page import JunoJacketPage
from .locators import JacketsWomenLocators
from .locators import CartWindowLocators
from .locators import SuccessfulMessageLOCATORS
from .cart_page import CartPage
import time

class JacketsWomenPage(BasePage):
    def customer_can_go_to_olivia_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_NAME).click()
        return OliviaJacketPage(driver=self.driver, url=self.driver.current_url)

    def customer_can_go_to_juno_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.JUNO_NAME).click()
        return JunoJacketPage(driver=self.driver, url=self.driver.current_url)

    def choose_size_and_colour_then_add_olivia_jacket_to_cart(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_SIZE).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_COLOR).click()
        time.sleep(3)
        button = self.driver.find_element(*JacketsWomenLocators.BUTTON_ADD_OLIVIA_TO_CART).click()
        time.sleep(5)

    def go_to_cart_page_from_successful_message(self):
        shopping_cart_link = self.driver.find_element(*SuccessfulMessageLOCATORS.LINK_TO_CART_FROM_OLIVIA_MESSAGE)
        shopping_cart_link.click()
        return CartPage(driver=self.driver, url=self.driver.current_url)
    def see_successful_message_after_adding_olivia_jacket(self):
        message_element = self.driver.find_element(*SuccessfulMessageLOCATORS.OLIVIA_MESSAGE)
        assert message_element.text == "You added Olivia 1/4 Zip Light Jacket to your shopping cart.", "Olivia jacket not added to cart"

    def choose_size_and_colour_then_add_juno_jacket_to_cart(self):
        self.driver.find_element(*JacketsWomenLocators.JUNO_SIZE).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.JUNO_COLOR).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.BUTTON_ADD_JUNO_TO_CART).click()
        time.sleep(3)
        message_element = self.driver.find_element(*SuccessfulMessageLOCATORS.OLIVIA_MESSAGE)
        assert message_element.text == "You added Juno Jacket to your shopping cart.", "Juno jacket not added to cart"

    def go_to_cart_window(self):
        self.driver.find_element(*JacketsWomenLocators.SHOW_CART_WINDOW).click()
        time.sleep(3)

    def go_to_cart_page_from_cart_window(self):
        show_cart = self.driver.find_element(*JacketsWomenLocators.VIEW_CART_PAGE).click()
        return CartPage(driver=self.driver, url=self.driver.current_url)

    def check_jacket_name_in_cart(self):
        name_element = self.driver.find_element(*CartWindowLocators.NAME)
        assert name_element.text == "Olivia 1/4 Zip Light Jacket", "Olivia name is not presented in cart"

    def check_quantity_of_jackets_in_cart(self):
        quantity_element = self.driver.find_element(*CartWindowLocators.Quantity)
        assert quantity_element.text == '1', "Quantity of jackets is not 1"

    def check_size_of_jacket_in_cart(self):
        button_see_details = self.driver.find_element(*CartWindowLocators.SEE_DETAILS).click()
        size_element = self.driver.find_element(*CartWindowLocators.SIZE)
        assert size_element.text == "M", "Size M is not presented in cart"

    def check_color_of_jacket_in_cart(self):
        button_see_details = self.driver.find_element(*CartWindowLocators.SEE_DETAILS).click()
        color_element = self.driver.find_element(*CartWindowLocators.COLOR)
        assert color_element.text == "Purple", "Purple jacket is not presented in cart"


