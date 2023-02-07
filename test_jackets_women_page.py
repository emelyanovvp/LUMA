import time
from .jackets_women_page import JacketsWomenPage
from .olivia_jacket_page import OliviaJacketPage
from .juno_jacket_page import JunoJacketPage
from .cart_page import CartPage
import pytest
from selenium.webdriver.common.by import By
from .cart_page import CartPage

def test_customer_can_go_to_olivia_jacket_page(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.customer_can_go_to_olivia_jacket_page()
    assert "olivia" in driver.current_url, "Olivia jacket page is not presented"

def test_customer_can_go_to_juno_jacket_page(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.customer_can_go_to_juno_jacket_page()
    assert "juno" in driver.current_url, "Juno jacket page is not presented"

def test_customer_can_choose_size_and_colour_then_add_olivia_jacket_to_cart(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()

def test_customer_can_choose_size_and_colour_then_add_juno_jacket_to_cart(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_juno_jacket_to_cart()

def test_should_be_proper_jacket_name(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_product_to_cart()
    page.go_to_cart_window()
    page.check_jacket_name_in_cart()

def test_should_be_proper_quantity_of_jackets(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_product_to_cart()
    page.go_to_cart_window()
    page.check_quantity_of_jackets_in_cart()

def test_should_be_proper_size_of_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_product_to_cart()
    page.go_to_cart_window()
    page.check_size_of_jacket()

def test_should_be_proper_color_of_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_product_to_cart()
    page.go_to_cart_window()
    page.check_color_of_jacket()

if __name__ == "__main__":
    pytest.main()