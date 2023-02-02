from .login_page import LoginPage
import pytest
from selenium.webdriver.common.by import By

def test_after_sign_in_customer_go_to_my_account_page(driver):
    url = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/"
    page = LoginPage(driver,url)
    page.open()
    page.customer_can_put_data_into_login_form_and_sign_in()
    assert "account" in driver.current_url, "My account page is not presented"

if __name__ == '__main__':
    pytest.main()