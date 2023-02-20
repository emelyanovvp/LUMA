from .base_page import BasePage
from .olivia_jacket_page import OliviaJacketPage
from .juno_jacket_page import JunoJacketPage
from .neve_jacket_page import NeveJacketPage
from .nadia_jacket_page import NadiaJacketPage
from .locators import JacketsWomenLocators
from .locators import CartWindowLocators
from .locators import SuccessfulMessageLOCATORS
from .cart_page import CartPage
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class JacketsWomenPage(BasePage):


    def view_as_list(self):
        self.driver.find_element(*JacketsWomenLocators.VIEW_AS_LIST_BUTTON).click()
        return JacketsWomenPage(driver=self.driver,url=self.driver.current_url)
    def view_as_grid(self):
        self.driver.find_element(*JacketsWomenLocators.VIEW_AS_GRID_BUTTON).click()
        return JacketsWomenPage(driver=self.driver,url=self.driver.current_url)

    def customer_can_go_to_olivia_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_NAME).click()
        return OliviaJacketPage(driver=self.driver, url=self.driver.current_url)
    def customer_can_go_to_juno_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.JUNO_NAME).click()
        return JunoJacketPage(driver=self.driver, url=self.driver.current_url)
    def customer_can_go_to_neve_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.NEVE_NAME).click()
        return NeveJacketPage(driver=self.driver, url=self.driver.current_url)
    def customer_can_go_to_nadia_jacket_page(self):
        self.driver.find_element(*JacketsWomenLocators.NADIA_NAME).click()
        return NadiaJacketPage(driver=self.driver, url=self.driver.current_url)
    def go_to_cart_page_from_successful_message(self):
        shopping_cart_link = self.driver.find_element(*SuccessfulMessageLOCATORS.LINK_TO_CART_FROM_SUCCESS_MESSAGE)
        shopping_cart_link.click()
        return CartPage(driver=self.driver, url=self.driver.current_url)
    def see_successful_message_after_adding_olivia_jacket(self):
        message_element = self.driver.find_element(*SuccessfulMessageLOCATORS.SUCCESS_MESSAGE)
        assert message_element.text == "You added Olivia 1/4 Zip Light Jacket to your shopping cart.", "Olivia jacket not added to cart"
    def choose_size_and_colour_then_add_olivia_jacket_to_cart(self):
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_SIZE_M).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.OLIVIA_COLOR_PURPLE).click()
        time.sleep(3)
        button = self.driver.find_element(*JacketsWomenLocators.BUTTON_ADD_OLIVIA_TO_CART).click()
        time.sleep(5)
        message_element = self.driver.find_element(*SuccessfulMessageLOCATORS.SUCCESS_MESSAGE)
        assert message_element.text == "You added Olivia Jacket to your shopping cart.", "Olivia jacket not added to cart"
    def choose_size_and_colour_then_add_juno_jacket_to_cart(self):
        self.driver.find_element(*JacketsWomenLocators.JUNO_SIZE_S).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.JUNO_COLOR_GREEN).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.BUTTON_ADD_JUNO_TO_CART).click()
        time.sleep(3)
        message_element = self.driver.find_element(*SuccessfulMessageLOCATORS.SUCCESS_MESSAGE)
        assert message_element.text == "You added Juno Jacket to your shopping cart.", "Juno jacket not added to cart"
    def choose_size_and_colour_then_add_neve_jacket_to_cart(self):
        self.driver.find_element(*JacketsWomenLocators.NEVE_SIZE_XS).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.NEVE_COLOR_BLACK).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.BUTTON_ADD_NEVE_TO_CART).click()
        time.sleep(3)
        message_element = self.driver.find_element(*SuccessfulMessageLOCATORS.SUCCESS_MESSAGE)
        assert message_element.text == "You added Neve Studio Dance Jacket to your shopping cart.", "Juno jacket not added to cart"
    def choose_size_and_colour_then_add_nadia_jacket_to_cart(self):
        self.driver.find_element(*JacketsWomenLocators.NADIA_SIZE_XS).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.NADIA_COLOR_BLACK).click()
        time.sleep(3)
        self.driver.find_element(*JacketsWomenLocators.BUTTON_ADD_NADIA_TO_CART).click()
        time.sleep(3)
        message_element = self.driver.find_element(*SuccessfulMessageLOCATORS.SUCCESS_MESSAGE)
        assert message_element.text == "You added Nadia Elements Shell to your shopping cart.", "Nadia jacket not added to cart"

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

    def all_size_and_color_buttons_should_be_clickable_for_olivia_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_COLOR_BLACK), \
            "Black button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_COLOR_BLUE), \
            "Blue button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.OLIVIA_COLOR_PURPLE),\
            "Purple button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_juno_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_COLOR_BLUE), \
            "Blue button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_COLOR_GREEN), \
            "Green button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JUNO_COLOR_PURPLE),\
            "Purple button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_neve_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_COLOR_BLACK), \
            "Black button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_COLOR_BLUE), \
            "Blue button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NEVE_COLOR_ORANGE),\
            "Orange button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_nadia_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_COLOR_BLACK), \
            "Black button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_COLOR_ORANGE), \
            "Orange button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.NADIA_COLOR_YELLOW),\
            "Yellow button is not clickable"

    def all_size_and_color_buttons_should_be_clickable_for_jade_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_COLOR_BLUE), \
            "Blue button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_COLOR_GRAY), \
            "Gray button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JADE_COLOR_GREEN),\
            "Green button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_adrienne_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_COLOR_GRAY), \
            "Gray button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_COLOR_ORANGE), \
            "Orange button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.ADRIENNE_COLOR_PURPLE),\
            "Purple button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_inez_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_COLOR_ORANGE), \
            "Orange button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_COLOR_PURPLE), \
            "Purple button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INEZ_COLOR_RED),\
            "Red button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_riona_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_COLOR_BROWN), \
            "Brown button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_COLOR_GREEN), \
            "Green button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.RIONA_COLOR_RED),\
            "Red button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_ingrid_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_COLOR_ORANGE), \
            "Orange button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_COLOR_RED), \
            "Red button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.INGRID_COLOR_WHITE),\
            "White button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_augusta_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_COLOR_BLUE), \
            "Blue button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_COLOR_ORANGE), \
            "Orange button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.AUGUSTA_COLOR_RED),\
            "Red button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_josie_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_SIZE_XS), \
            "XS button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_SIZE_XL), \
            "XL button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_COLOR_BLACK), \
            "Black button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_COLOR_BLUE), \
            "Blue button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.JOSIE_COLOR_GRAY),\
            "Gray button is not clickable"
    def all_size_and_color_buttons_should_be_clickable_for_stellar_jacket(self):
        assert self.is_element_clickable(*JacketsWomenLocators.STELLAR_SIZE_S), \
            "S button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.STELLAR_SIZE_M), \
            "M button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.STELLAR_SIZE_L), \
            "L button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.STELLAR_COLOR_BLUE), \
            "Blue button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.STELLAR_COLOR_RED), \
            "Red button is not clickable"
        assert self.is_element_clickable(*JacketsWomenLocators.STELLAR_COLOR_YELLOW), \
            "Yellow button is not clickable"







