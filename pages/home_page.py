from .base_page import BasePage
from .locators import BasePageLocators
from .locators import HomePageLocators
from .login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from .gear_page import GearPage
from .men_page import MenPage
from .women_page import WomenPage
from .tops_women_page import TopsWomenPage
from .bottoms_women_page import BottomsWomenPage
from .jackets_women_page import JacketsWomenPage
from .hoodies_women_page import HoodiesWomenPage
from .tees_women_page import TeesWomenPage
from .bras_women_page import BrasWomenPage
from .pants_women_page import PantsWomenPage
from .shorts_women_page import ShortsWomenPage
from .sale_page import SalePage
from .training_page import TrainingPage
from .whats_new_page import WhatsNewPage
from .new_yoga_page import NewYogaPage
from .pants_page import PantsPage
from .erin_page import ErinPage
from .tees_page import TeesPage
from .performance_page import PerformancePage
from .eco_page import EcoPage

class HomePage(BasePage) :
    def click_link_sign_in_and_go_to_login_page(self):
        self.driver.find_element(*BasePageLocators.SIGN_IN_LINK).click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)
    def click_link_create_account_and_go_to_regform_page(self):
        self.driver.find_element(*BasePageLocators.CREATE_ACCOUNT_LINK).click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)
    def go_to_whats_new_page(self):
        self.driver.find_element(*BasePageLocators.WHATS_NEW).click()
        return WhatsNewPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_page(self):
        self.driver.find_element(*BasePageLocators.WOMEN).click()
        return WomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_tops_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_TOPS_LINK).click()
        return TopsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_jackets_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        select_tops = self.driver.find_element(*BasePageLocators.WOMEN_TOPS_LINK)
        ActionChains(self.driver).move_to_element(select_tops).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_TOPS_JACKETS_LINK).click()
        return JacketsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_hoodies_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        select_tops = self.driver.find_element(*BasePageLocators.WOMEN_TOPS_LINK)
        ActionChains(self.driver).move_to_element(select_tops).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_TOPS_HOODIES_LINK).click()
        return HoodiesWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_tees_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        select_tops = self.driver.find_element(*BasePageLocators.WOMEN_TOPS_LINK)
        ActionChains(self.driver).move_to_element(select_tops).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_TOPS_TEES_LINK).click()
        return TeesWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_bras_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        select_tops = self.driver.find_element(*BasePageLocators.WOMEN_TOPS_LINK)
        ActionChains(self.driver).move_to_element(select_tops).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_TOPS_BRAS_LINK).click()
        return BrasWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_bottoms_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_BOTTOMS_LINK).click()
        return BottomsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_pants_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        select_bottoms = self.driver.find_element(*BasePageLocators.WOMEN_BOTTOMS_LINK)
        ActionChains(self.driver).move_to_element(select_bottoms).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_BOTTOMS_PANTS_LINK).click()
        return PantsWomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_shorts_page_from_home_page(self):
        select_women = self.driver.find_element(*BasePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select_women).perform()
        select_bottoms = self.driver.find_element(*BasePageLocators.WOMEN_BOTTOMS_LINK)
        ActionChains(self.driver).move_to_element(select_bottoms).perform()
        self.driver.find_element(*BasePageLocators.WOMEN_BOTTOMS_SHORTS_LINK).click()
        return ShortsWomenPage(driver=self.driver, url=self.driver.current_url)

    def go_to_men_page(self):
        self.driver.find_element(*BasePageLocators.MEN).click()
        return MenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_gear_page(self):
        self.driver.find_element(*BasePageLocators.GEAR).click()
        return GearPage(driver=self.driver, url=self.driver.current_url)
    def go_to_training_page(self):
        self.driver.find_element(*BasePageLocators.TRAINING).click()
        return TrainingPage(driver=self.driver, url=self.driver.current_url)
    def go_to_sale_page(self):
        self.driver.find_element(*BasePageLocators.SALE).click()
        return SalePage(driver=self.driver, url=self.driver.current_url)

    def go_to_new_yoga_page(self):
        self.driver.find_element(*HomePageLocators.SHOP_NEW_YOGA).click()
        return NewYogaPage(driver=self.driver, url=self.driver.current_url)
    def go_to_pants_page(self):
        self.driver.find_element(*HomePageLocators.SHOP_PANTS).click()
        return PantsPage(driver=self.driver, url=self.driver.current_url)
    def go_to_erin_page(self):
        self.driver.find_element(*HomePageLocators.SHOP_ERIN_RECOMMENDS).click()
        return ErinPage(driver=self.driver, url=self.driver.current_url)
    def go_to_tees_page(self):
        self.driver.find_element(*HomePageLocators.SHOP_TEES).click()
        return TeesPage(driver=self.driver, url=self.driver.current_url)
    def go_to_performance_page(self):
        self.driver.find_element(*HomePageLocators.SHOP_PERFORMANCE).click()
        return PerformancePage(driver=self.driver, url=self.driver.current_url)
    def go_to_eco_page(self):
        self.driver.find_element(*HomePageLocators.SHOP_ECO_FRIENDLY).click()
        return EcoPage(driver=self.driver, url=self.driver.current_url)
