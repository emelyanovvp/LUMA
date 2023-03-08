from .pages.create_account_page import CreateAccountPage
from .pages.locators import CreateAccountLocators
import pytest

def test_see_message_no_password_before_putting_symbols(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    password_strength_message = page.there_is_password_strength_message()
    assert password_strength_message == "No Password", "No password strength message"

def test_see_message_weak_during_putting_less_than_8_symbols(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    page.put_less_than_8_symbols()
    text_message = page.there_is_password_strength_message()
    assert text_message == "Weak", "No password strength message"

def test_see_message_weak_during_putting_more_than_7_but_improper_symbols(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    page.put_more_than_7_but_improper_symbols()
    text_message = page.there_is_password_strength_message()
    assert text_message == "Weak", "No password strength message"

def test_see_message_medium_during_putting_proper_symbols_enough_for_medium_password(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    page.put_proper_symbols_enough_for_medium_password()
    text_message = page.there_is_password_strength_message()
    assert text_message == "Medium", "No password strength message"

def test_see_message_strong_after_putting_proper_symbols_enough_for_strong_password(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    page.put_proper_symbols_enough_for_strong_password()
    text_message = page.there_is_password_strength_message()
    assert text_message == "Strong", "No password strength message"

def test_see_info_during_putting_less_than_8_symbols(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    page.put_less_than_8_symbols()
    page.put_less_than_8_symbols()
    text_info = page.there_is_password_info()
    assert text_info == "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.", "No such password info is presented"

def test_see_info_during_putting_more_than_7_but_improper_symbols(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    page.put_less_than_8_symbols()
    page.put_more_than_7_but_improper_symbols()
    text_info = page.there_is_password_info()
    assert text_info == "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters.", "No such password info is presented"
@pytest.mark.smoke
def test_see_no_info_after_putting_proper_symbols_enough_for_medium_or_strong_password(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver, url)
    page.open()
    page.put_proper_symbols_enough_for_medium_password()
    page.put_proper_symbols_enough_for_strong_password()
    try:
        text_info = page.there_is_password_info()
        assert False
    except:
        assert True

def test_after_registration_customer_go_to_my_account_page(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver,url)
    page.open()
    page.customer_can_put_data_into_create_account_form_and_sign_in()
    assert "account" in driver.current_url, "My account page is not presented"

if __name__ == '__main__':
    pytest.main()
