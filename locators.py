from selenium.webdriver.common.by import By

class HomePageLocators():
    SIGN_IN_LINK = (By.CSS_SELECTOR, ".authorization-link")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[text()='Create an Account']")
