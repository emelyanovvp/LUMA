
from .base_page import BasePage
from .my_account_page import MyAccountPage
from .locators import CreateAccountLocators

class CreateAccountPage(BasePage):
    def customer_can_put_data_into_create_account_form_and_sign_in(self):
        self.driver.find_element(*CreateAccountLocators.FIRST_NAME).send_keys("Greg")
        self.driver.find_element(*CreateAccountLocators.LAST_NAME).send_keys("Gregorov")
        self.driver.find_element(*CreateAccountLocators.EMAIL).send_keys("greg@gmail.com")
        self.driver.find_element(*CreateAccountLocators.PASSWORD).send_keys("123456GREG&greg")
        self.driver.find_element(*CreateAccountLocators.PASSWORD_CONFIRMATION).send_keys("123456GREG&greg")
        self.driver.find_element(*CreateAccountLocators.BUTTON_CREATE_ACCOUNT).click()
        return MyAccountPage(driver=self.driver, url=self.driver.current_url)




