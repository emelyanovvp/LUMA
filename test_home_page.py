from .home_page import HomePage
import pytest
from selenium.webdriver.common.by import By

def test_customer_can_go_to_login_page_from_sign_in_link(driver):
    url = "https://magento.softwaretestingboard.com/"
    home_page = HomePage(driver, url)
    home_page.open()
    home_page.click_link_sign_in_and_go_to_login_page()
    assert "login" in driver.current_url , "Login page is not presented"

def test_customer_can_go_to_regform_page_from_create_account_link(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.click_link_create_account_and_go_to_regform_page()
    assert "create" in driver.current_url, "Registration form page is not presented"

def test_customer_can_go_to_women_tops_jackets_link_and_click(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.move_mouse_to_women_tops_jackets_link_and_click()
    assert "jackets-women" in driver.current_url, "Women jackets page is not presented"


if __name__ == '__main__':
    pytest.main()
