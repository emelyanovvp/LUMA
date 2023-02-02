from selenium.webdriver.common.by import By

class HomePageLocators():
    SIGN_IN_LINK = (By.CSS_SELECTOR, ".authorization-link")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[text()='Create an Account']")
    WOMEN_LINK = (By.CSS_SELECTOR,".ui-menu-icon")
    WOMEN_TOPS_LINK = (By.CSS_SELECTOR,"a#ui-id-9>span:nth-child(2)")
    WOMEN_TOPS_JACKETS_LINK = (By.CSS_SELECTOR,"a#ui-id-11>span")
class CreateAccountLocators():
    FIRST_NAME = (By.CSS_SELECTOR,"input#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastname")
    EMAIL = (By.CSS_SELECTOR,"input#email_address")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "input#password-confirmation")
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR,"button.primary>span")
class LoginPageLocators():
    INPUT_EMAIL = (By.CSS_SELECTOR, "input#email")
    INPUT_PASS = (By.CSS_SELECTOR, "input#pass")
    SIGN_IN = (By.CSS_SELECTOR,"#send2>span")