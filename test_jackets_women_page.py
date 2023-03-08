import time
from .pages.jackets_women_page import JacketsWomenPage
from .pages.base_page import BasePage
from .pages.locators import JacketsWomenLocators
from .pages.locators import BasePageLocators
import pytest


def test_all_style_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_style_types_should_be_clickable()

def test_all_size_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_types_should_be_clickable()

def test_all_price_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_price_types_should_be_clickable()

def test_all_color_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_color_types_should_be_clickable()

def test_all_material_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_material_types_should_be_clickable()

def test_all_eco_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_eco_types_should_be_clickable()

def test_all_performance_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_performance_types_should_be_clickable()
def test_all_erin_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_erin_types_should_be_clickable()

def test_all_new_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_new_types_should_be_clickable()

def test_all_sale_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_sale_types_should_be_clickable()
@pytest.mark.smoke
def test_all_pattern_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_pattern_types_should_be_clickable()
@pytest.mark.smoke
def test_all_climate_types_should_be_clickable(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_climate_types_should_be_clickable()




def test_sort_by_ascending_position(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html?product_list_dir=desc"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.sort_by_ascending_position(*BasePageLocators.ASCENDING_DIRECTION_SIGN)
    assert "product_list_dir=desc" not in driver.current_url, "Ascending position is not presented"

def test_sort_by_descending_position(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.sort_by_descending_position(*BasePageLocators.DESCENDING_DIRECTION_SIGN)
    assert "product_list_dir=desc" in driver.current_url, "Descending position is not presented"

def test_sort_by_product_position(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.sort_by_product_position(*BasePageLocators.SELECT_POSITION)
    assert "product_list_order=name" not in driver.current_url or "product_list_order=price" not in driver.current_url, \
        "By position selection is not presented"
def test_sort_by_product_price(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.sort_by_product_price(*BasePageLocators.SELECT_POSITION)
    assert "product_list_order=price" in driver.current_url, "By price selection is not presented"
def test_sort_by_product_name(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.sort_by_product_name(*BasePageLocators.SELECT_POSITION)
    assert "product_list_order=name" in driver.current_url, "By name selection is not presented"

def test_is_expected_page_title_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*BasePageLocators.TITLE_ELEMENT) == 'Jackets', \
        "Expected title is not presented"

def test_is_element_shopping_options_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*BasePageLocators.SHOPPING_OPTIONS) == "Shopping Options", \
        "Shopping options is not presented"

def test_is_element_12_items_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*BasePageLocators.ITEMS_AMOUNT) == "12", \
        "Expected amount is not presented"

def test_view_as_grid(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.view_as_grid()
    assert "product_list_mode=list" not in driver.current_url, "Grid view button is not presented"

def test_view_as_list(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.view_as_list()
    assert "product_list_mode=list" in driver.current_url, "List view button is not presented"

def test_go_to_cart_window_after_adding_item_to_cart(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()
    time.sleep(3)
    assert page.can_see_cart_window() == "Proceed to Checkout", "Cart window is not presented"

def test_can_go_to_cart_page_from_cart_window(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()
    time.sleep(3)
    page.can_see_cart_window()
    time.sleep(3)
    page.go_to_cart_page_from_cart_window()
    assert "cart" in driver.current_url, "Cart window is not presented"

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

def test_customer_can_go_to_neve_jacket_page(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.customer_can_go_to_neve_jacket_page()
    assert "neve" in driver.current_url, "Neve jacket page is not presented"

def test_customer_can_go_to_nadia_jacket_page(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.customer_can_go_to_nadia_jacket_page()
    assert "nadia" in driver.current_url, "Nadia jacket page is not presented"
def test_go_to_cart_page_from_successfull_message(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()
    page.go_to_cart_page_from_successful_message()
    assert "cart" in driver.current_url, "Cart page is not presented"

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

def test_customer_can_choose_size_and_colour_then_add_neve_jacket_to_cart(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_neve_jacket_to_cart()

def test_customer_can_choose_size_and_colour_then_add_nadia_jacket_to_cart(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_nadia_jacket_to_cart()
def test_should_be_proper_jacket_name(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()
    page.go_to_cart_window()
    page.check_jacket_name_in_cart()
def test_should_be_proper_quantity_of_jackets(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()
    page.go_to_cart_window()
    page.check_quantity_of_jackets_in_cart()
def test_should_be_proper_size_of_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()
    page.go_to_cart_window()
    page.check_size_of_jacket_in_cart()
def test_should_be_proper_color_of_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.choose_size_and_colour_then_add_olivia_jacket_to_cart()
    page.go_to_cart_window()
    page.check_color_of_jacket_in_cart()

def test_all_size_and_color_buttons_should_be_clickable_for_olivia_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_olivia_jacket()

def test_all_size_and_color_buttons_should_be_clickable_for_juno_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_juno_jacket()

def test_all_size_and_color_buttons_should_be_clickable_for_neve_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_neve_jacket()

def test_all_size_and_color_buttons_should_be_clickable_for_nadia_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_nadia_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_jade_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_jade_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_adrienne_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_adrienne_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_inez_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_inez_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_riona_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_riona_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_ingrid_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_ingrid_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_augusta_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_augusta_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_josie_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_josie_jacket()
def test_all_size_and_color_buttons_should_be_clickable_for_stellar_jacket(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    page.all_size_and_color_buttons_should_be_clickable_for_stellar_jacket()

if __name__ == "__main__":
    pytest.main()