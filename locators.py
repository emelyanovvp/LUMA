from selenium.webdriver.common.by import By

class HomePageLocators():
    SIGN_IN_LINK = (By.CSS_SELECTOR, ".authorization-link")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[text()='Create an Account']")

    WOMEN_LINK = (By.CSS_SELECTOR,".ui-menu-icon")
    WOMEN_TOPS_LINK = (By.CSS_SELECTOR,"a#ui-id-9>span:nth-child(2)")
    WOMEN_TOPS_JACKETS_LINK = (By.CSS_SELECTOR,"a#ui-id-11>span")

