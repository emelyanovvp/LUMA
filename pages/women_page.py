from .base_page import BasePage
from .locators import WomenPageLocators
from .tops_women_page import TopsWomenPage
from .bottoms_women_page import BottomsWomenPage
from .hoodies_women_page import HoodiesWomenPage
from .jackets_women_page import JacketsWomenPage
from .tees_women_page import TeesWomenPage
from .brass_women_page import BrassWomenPage
from .pants_women_page import PantsWomenPage
from .shorts_women_page import ShortsWomenPage
class WomenPage(BasePage):
    def go_to_tops_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_TOPS_LINK).click()
        return TopsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_bottoms_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_BOTTOMS_LINK).click()
        return BottomsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_hoodies_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_HOODIES_LINK).click()
        return HoodiesWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_jackets_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_JACKETS_LINK).click()
        return JacketsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_tees_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_TEES_LINK).click()
        return TeesWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_brass_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_BRASS_LINK).click()
        return BrassWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_pants_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_PANTS_LINK).click()
        return PantsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_shorts_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_SHORTS_LINK).click()
        return ShortsWomenPage(driver=self.driver, url=self.driver.current_url)