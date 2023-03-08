import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from selenium.webdriver.support.ui import Select
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
    def sort_by_product_name(self,how,what):
        select = Select(self.driver.find_element(how,what))
        select.select_by_value("name")

    def sort_by_product_price(self, how, what):
        select = Select(self.driver.find_element(how, what))
        select.select_by_value("price")
    def sort_by_product_position(self, how, what):
        select = Select(self.driver.find_element(how, what))
        select.select_by_value("position")

    def sort_by_descending_position(self,how,what):
       self.driver.find_element(how,what).click()
       time.sleep(2)
    def sort_by_ascending_position(self,how,what):
       self.driver.find_element(how,what).click()
       time.sleep(2)
    def view_as_list(self):
        self.driver.find_element(*BasePageLocators.VIEW_AS_LIST_BUTTON).click()
        time.sleep(2)

    def view_as_grid(self):
        self.driver.find_element(*BasePageLocators.VIEW_AS_GRID_BUTTON).click()
        time.sleep(2)

    def can_see_cart_window(self):
        self.driver.find_element(*BasePageLocators.SHOW_CART_WINDOW).click()
        time.sleep(2)
        element = self.driver.find_element(*BasePageLocators.PROCEED_TO_CHECKOUT)
        return element.text

    def go_to_cart_page_from_cart_window(self):
        show_cart = self.driver.find_element(*BasePageLocators.VIEW_CART_PAGE).click()
        time.sleep(3)

    def all_style_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.STYLE_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_INSULATED), \
            "Insulated link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_JACKET), \
            "Jacket link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_LIGHTWIEGHT), \
            "Lightweight link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_HOODED), \
            "Hooded link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_HEAVY), \
            "Heavy link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_RAIN), \
            "Rain link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_HARD), \
            "Hard link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_SOFT), \
            "Soft link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_WINDBREAKER), \
            "Windbreaker link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_QUARTER_ZIP), \
            "Quarter zip link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_FULL_ZIP), \
            "Full zip link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.STYLE_FILTER_REVERSIBLE), \
            "Reversible link is not clickable"
    def all_size_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.SIZE_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.SIZE_FILTER_XS), \
            "XS link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.SIZE_FILTER_S), \
            "S link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.SIZE_FILTER_M), \
            "M link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.SIZE_FILTER_L), \
            "L link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.SIZE_FILTER_XL), \
            "XL link is not clickable"
    def all_price_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.PRICE_FILTER).click()
        time.sleep(5)
        assert self.is_element_clickable(*BasePageLocators.PRICE_FILTER_30_40), \
            "30-40 link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.PRICE_FILTER_50_60), \
            "50-60 link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.PRICE_FILTER_60_70), \
            "60-70 link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.PRICE_FILTER_70_80), \
            "70-80 link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.PRICE_FILTER_above_80), \
            "Above 80 link is not clickable"
    def all_color_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.COLOR_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_BLACK), \
            "Black link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_BLUE), \
            "Blue link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_BROWN), \
            "Brown link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_GREY), \
            "Grey link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_GREEN), \
            "Green link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_ORANGE), \
            "Orange link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_PURPLE), \
            "Purple link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_RED), \
            "Red link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_WHITE), \
            "White link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.COLOR_FILTER_YELLOW), \
            "Yellow link is not clickable"
    def all_material_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.MATERIAL_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.FILTER_COCONA), \
            "Cocona link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_COTTON), \
            "Cotton link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_FLEECE), \
            "Fleece link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_LUMATECH), \
            "Lumatech link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_MESH), \
            "Mesh link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_LYCRA), \
            "Lycra link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_NYLON), \
            "Nylon link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_POLYESTER), \
            "Polyester link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_SPANDEX), \
            "Spandex link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_COOLTECH), \
            "Cooltech link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.FILTER_WOOL), \
            "Wool link is not clickable"
    def all_eco_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.ECO_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.ECO_YES), \
            "Yes link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.ECO_NO), \
            "No link is not clickable"
    def all_performance_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.PERFORMANCE_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.PERFORMANCE_YES), \
            "Yes link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.PERFORMANCE_NO), \
            "No link is not clickable"
    def all_erin_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.ERIN_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.ERIN_YES), \
            "Yes link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.ERIN_NO), \
            "No link is not clickable"
    def all_new_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.NEW_FILTER).click()
        time.sleep(5)
        assert self.is_element_clickable(*BasePageLocators.NEW_YES), \
            "Yes link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.NEW_NO), \
            "No link is not clickable"
    def all_sale_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.SALE_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.SALE_YES), \
            "Yes link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.SALE_NO), \
            "No link is not clickable"
    def all_pattern_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.PATTERN_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.PATTERN_COLOR_BLOCKED), \
            "Color-blocked link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.PATTERN_SOLID), \
            "Solid link is not clickable"
    def all_climate_types_should_be_clickable(self):
        self.driver.find_element(*BasePageLocators.CLIMATE_FILTER).click()
        time.sleep(3)
        assert self.is_element_clickable(*BasePageLocators.CLIMATE_ALL_WEATHER), \
            "All-weather link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.CLIMATE_COLD), \
            "Cold link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.CLIMATE_COOL), \
            "Cool link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.CLIMATE_INDOOR), \
            "Indoor link is not clickable"
        assert self.is_element_clickable(*BasePageLocators.CLIMATE_MILD), \
            "Mild link is not clickable"
