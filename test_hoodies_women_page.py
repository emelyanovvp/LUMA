from .pages.hoodies_women_page import HoodiesWomenPage
from .pages.base_page import BasePage
from .pages.locators import HoodiesWomenLocators
from .pages.locators import BasePageLocators
import pytest

def test_sort_by_ascending_position(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html?product_list_dir=desc"
    page = HoodiesWomenPage(driver, url)
    page.open()
    page.sort_by_ascending_position(*BasePageLocators.ASCENDING_DIRECTION_SIGN)
    assert "product_list_dir=desc" not in driver.current_url, "Ascending position is not presented"
def test_sort_by_descending_position(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    page.sort_by_descending_position(*BasePageLocators.DESCENDING_DIRECTION_SIGN)
    assert "product_list_dir=desc" in driver.current_url, "Descending position is not presented"

def test_sort_by_product_position(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    page.sort_by_product_position(*BasePageLocators.SELECT_POSITION)
    assert "product_list_order=name" not in driver.current_url or "product_list_order=price" not in driver.current_url, \
        "By position selection is not presented"

def test_sort_by_product_price(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    page.sort_by_product_price(*BasePageLocators.SELECT_POSITION)
    assert "product_list_order=price" in driver.current_url, "By price selection is not presented"

def test_sort_by_product_name(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    page.sort_by_product_name(*BasePageLocators.SELECT_POSITION)
    assert "product_list_order=name" in driver.current_url, "By name selection is not presented"

def test_is_expected_page_title_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*BasePageLocators.TITLE_ELEMENT) == 'Hoodies & Sweatshirts', \
        "Expected title is not presented"

def test_is_element_shopping_options_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*BasePageLocators.SHOPPING_OPTIONS) == "Shopping Options", \
        "Shopping options is not presented"

def test_is_element_12_items_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*BasePageLocators.ITEMS_AMOUNT) == "12", \
        "Expected amount is not presented"
@pytest.mark.smoke
def test_view_as_grid(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    page.view_as_grid()
    assert "product_list_mode=list" not in driver.current_url, "Grid view button is not presented"
@pytest.mark.smoke
def test_view_as_list(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
    page = HoodiesWomenPage(driver, url)
    page.open()
    page.view_as_list()
    assert "product_list_mode=list" in driver.current_url, "List view button is not presented"