from .pages.create_account_page import CreateAccountPage
import pytest


def test_after_registration_customer_go_to_my_account_page(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    page = CreateAccountPage(driver,url)
    page.open()
    page.customer_can_put_data_into_create_account_form_and_sign_in()
    assert "account" in driver.current_url, "My account page is not presented"

if __name__ == '__main__':
    pytest.main()
