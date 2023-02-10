from .base_page import BasePage
from .locators import HomePageLocators
from .login_page import LoginPage
from .jackets_women_page import JacketsWomenPage
from selenium.webdriver.common.action_chains import ActionChains
from .gear_page import GearPage
from .men_page import MenPage
from .women_page import WomenPage
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
        self.driver.find_element(*HomePageLocators.SIGN_IN_LINK).click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def click_link_create_account_and_go_to_regform_page(self):
        self.driver.find_element(*HomePageLocators.CREATE_ACCOUNT_LINK).click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def move_mouse_to_women_tops_jackets_link_and_click(self):
        select1 = self.driver.find_element(*HomePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select1).perform()
        select2 = self.driver.find_element(*HomePageLocators.WOMEN_TOPS_LINK)
        ActionChains(self.driver).move_to_element(select2).perform()
        select3 = self.driver.find_element(*HomePageLocators.WOMEN_TOPS_JACKETS_LINK).click()
        return JacketsWomenPage(driver=self.driver, url=self.driver.current_url)

    def go_to_whats_new_page(self):
        self.driver.find_element(*HomePageLocators.WHATS_NEW).click()
        return WhatsNewPage(driver=self.driver, url=self.driver.current_url)
    def go_to_women_page(self):
        self.driver.find_element(*HomePageLocators.WOMEN).click()
        return WomenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_men_page(self):
        self.driver.find_element(*HomePageLocators.MEN).click()
        return MenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_gear_page(self):
        self.driver.find_element(*HomePageLocators.GEAR).click()
        return GearPage(driver=self.driver, url=self.driver.current_url)
    def go_to_training_page(self):
        self.driver.find_element(*HomePageLocators.TRAINING).click()
        return TrainingPage(driver=self.driver, url=self.driver.current_url)
    def go_to_sale_page(self):
        self.driver.find_element(*HomePageLocators.SALE).click()
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
