import pytest
from selenium.webdriver.common.by import By
from .cart_page import CartPage

def test_should_be_proper_product_name(driver):
    url = "https://magento.softwaretestingboard.com/checkout/cart/"
    page = CartPage(driver, url)
    page.open()
    real_name = page.should_be_proper_product_name()
    assert "olivia" in real_name, "Olivia name is not presented"
