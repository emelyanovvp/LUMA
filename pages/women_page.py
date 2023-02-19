from .base_page import BasePage
from .locators import WomenPageLocators
from .tops_women_page import TopsWomenPage
from .bottoms_women_page import BottomsWomenPage
from .hoodies_women_page import HoodiesWomenPage
from .jackets_women_page import JacketsWomenPage
from .tees_women_page import TeesWomenPage
from .bras_women_page import BrasWomenPage
from .pants_women_page import PantsWomenPage
from .shorts_women_page import ShortsWomenPage
class WomenPage(BasePage):
    def go_to_tops_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_TOPS_LINK_LEFT_BAR).click()
        return TopsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_bottoms_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_BOTTOMS_LINK_LEFT_BAR).click()
        return BottomsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_hoodies_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_HOODIES_LINK_LEFT_BAR).click()
        return HoodiesWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_jackets_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_JACKETS_LINK_LEFT_BAR).click()
        return JacketsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_tees_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_TEES_LINK_LEFT_BAR).click()
        return TeesWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_bras_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_BRAS_LINK_LEFT_BAR).click()
        return BrasWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_pants_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_PANTS_LINK_LEFT_BAR).click()
        return PantsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_shorts_women_page(self):
        self.driver.find_element(*WomenPageLocators.WOMEN_SHORTS_LINK_LEFT_BAR).click()
        return ShortsWomenPage(driver=self.driver, url=self.driver.current_url)



