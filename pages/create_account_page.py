
from .base_page import BasePage
from .my_account_page import MyAccountPage
from .locators import CreateAccountLocators
import time
class CreateAccountPage(BasePage):
    def put_less_than_8_symbols(self):
        self.driver.find_element(*CreateAccountLocators.PASSWORD).send_keys("123")
        time.sleep(1)
    def put_more_than_7_but_improper_symbols(self):
        self.driver.find_element(*CreateAccountLocators.PASSWORD).send_keys("123456789")
        time.sleep(1)
    def put_proper_symbols_enough_for_medium_password(self):
        self.driver.find_element(*CreateAccountLocators.PASSWORD).send_keys("12345abC")
        time.sleep(1)
    def put_proper_symbols_enough_for_strong_password(self):
        self.driver.find_element(*CreateAccountLocators.PASSWORD).send_keys("12345abCD")
        time.sleep(1)
    def there_is_password_strength_message(self):
        message = self.driver.find_element(*CreateAccountLocators.PASSWORD_STRENGTH)
        return message.text
    def there_is_password_info(self):
        info = self.driver.find_element(*CreateAccountLocators.PASSWORD_INFO)
        return info.text

    def customer_can_put_data_into_create_account_form_and_sign_in(self):
        self.driver.find_element(*CreateAccountLocators.FIRST_NAME).send_keys("Greg")
        self.driver.find_element(*CreateAccountLocators.LAST_NAME).send_keys("Gregorov")
        self.driver.find_element(*CreateAccountLocators.EMAIL).send_keys("greg@gmail.com")
        self.driver.find_element(*CreateAccountLocators.PASSWORD).send_keys("123456GREG&greg")
        self.driver.find_element(*CreateAccountLocators.PASSWORD_CONFIRMATION).send_keys("123456GREG&greg")
        self.driver.find_element(*CreateAccountLocators.BUTTON_CREATE_ACCOUNT).click()
        return MyAccountPage(driver=self.driver, url=self.driver.current_url)




