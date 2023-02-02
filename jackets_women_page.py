from .base_page import BasePage
from selenium.webdriver.common.by import By

class JacketsWomenPage(BasePage):
    def should_be_women_page(self):
        self.should_be_style_link()
        self.should_be_price_link()
        self.should_be_size_link()




