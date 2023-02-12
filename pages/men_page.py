from .base_page import BasePage
from .locators import MenPageLocators
from .tops_men_page import TopsMenPage
from .bottoms_men_page import BottomsMenPage
from .hoodies_men_page import HoodiesMenPage
from .jacket_men_page import JacketMenPage
from .tees_men_page import TeesMenPage
from .tanks_men_page import TanksMenPage
from .pants_men_page import PantsMenPage
from .shorts_men_page import ShortsMenPage

class MenPage(BasePage):
    def go_to_tops_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_TOPS_LINK).click()
        return TopsMenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_bottoms_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_BOTTOMS_LINK).click()
        return BottomsMenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_hoodies_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_HOODIES_LINK).click()
        return HoodiesMenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_jackets_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_JACKET_LINK).click()
        return JacketMenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_tees_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_TEES_LINK).click()
        return TeesMenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_tanks_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_TANKS_LINK).click()
        return TanksMenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_pants_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_PANTS_LINK).click()
        return PantsMenPage(driver=self.driver, url=self.driver.current_url)
    def go_to_shorts_men_page(self):
        self.driver.find_element(*MenPageLocators.MEN_SHORTS_LINK).click()
        return ShortsMenPage(driver=self.driver, url=self.driver.current_url)





