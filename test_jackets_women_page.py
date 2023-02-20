from .pages.jackets_women_page import JacketsWomenPage
from .pages.base_page import BasePage
from .pages.locators import JacketsWomenLocators
import pytest

@pytest.mark.smoke
def test_is_expected_page_title_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*JacketsWomenLocators.TITLE_ELEMENT) == 'Jackets', \
        "Expected title is not presented"

def test_is_element_shopping_options_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*JacketsWomenLocators.SHOPPING_OPTIONS) == "Shopping Options", \
        "Shopping options is not presented"

def test_is_element_12_items_presented(driver):
    url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    page = JacketsWomenPage(driver, url)
    page.open()
    assert page.is_expected_element_presented(*JacketsWomenLocators.ITEMS_AMOUNT) == "12", \
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