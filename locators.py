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

class JacketsWomenLocators():
    OLIVIA_NAME = (By.CSS_SELECTOR,"a.product-item-link")
    OLIVIA_SIZE = (By.CSS_SELECTOR,"#option-label-size-143-item-168")
    OLIVIA_COLOR = (By.CSS_SELECTOR,"#option-label-color-93-item-57")

    BUTTON_ADD_OLIVIA_TO_CART = (By.CSS_SELECTOR,"button.tocart>span")
    BUTTON_ADD_JUNO_TO_CART = (By.CSS_SELECTOR,"li:nth-child(2) .tocart>span")
    SHOW_CART_WINDOW = (By.CSS_SELECTOR,".showcart")
    VIEW_CART_PAGE = (By.CSS_SELECTOR,".viewcart>span")

    JUNO_NAME = (By.CSS_SELECTOR,"li:nth-child(2)  a.product-item-link")
    JUNO_SIZE = (By.CSS_SELECTOR,"li:nth-child(2) #option-label-size-143-item-167")
    JUNO_COLOR = (By.CSS_SELECTOR,"li:nth-child(2) #option-label-color-93-item-53")

class CartWindowLocators():
    NAME = (By.CSS_SELECTOR,".product-item-name>a")
    Quantity = (By.CSS_SELECTOR,"span.count")
    SEE_DETAILS = (By.CSS_SELECTOR, (".toggle>span"))
    SIZE = (By.CSS_SELECTOR,"dd.values:nth-child(2)")
    COLOR = (By.CSS_SELECTOR,"dd.values:nth-child(4)")
class SuccessfulMessageLOCATORS():
    OLIVIA_MESSAGE = (By.CSS_SELECTOR,".messages>.message-success>div")
    LINK_TO_CART_FROM_OLIVIA_MESSAGE = (By.CSS_SELECTOR,".messages>.message-success>div>a")