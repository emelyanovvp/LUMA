from selenium.webdriver.common.by import By
class BasePageLocators():
    SIGN_IN_LINK = (By.CSS_SELECTOR, ".authorization-link>a")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[text()='Create an Account']")
    WOMEN_LINK = (By.CSS_SELECTOR, "#ui-id-4>span:nth-child(2)")
    WOMEN_TOPS_LINK = (By.CSS_SELECTOR, "#ui-id-9>span:nth-child(2)")
    WOMEN_TOPS_JACKETS_LINK = (By.CSS_SELECTOR, "#ui-id-11>span")
    WOMEN_TOPS_HOODIES_LINK = (By.CSS_SELECTOR, "#ui-id-12>span")
    WOMEN_TOPS_TEES_LINK = (By.CSS_SELECTOR, "#ui-id-13>span")
    WOMEN_TOPS_BRAS_LINK = (By.CSS_SELECTOR, "#ui-id-14>span")
    WOMEN_BOTTOMS_LINK = (By.CSS_SELECTOR, "#ui-id-10>span:nth-child(2)")
    WOMEN_BOTTOMS_PANTS_LINK = (By.CSS_SELECTOR, "#ui-id-15>span")
    WOMEN_BOTTOMS_SHORTS_LINK = (By.CSS_SELECTOR, "#ui-id-16>span")
    MEN_LINK = (By.CSS_SELECTOR, "#ui-id-5>span:nth-child(2)")
    MEN_TOPS_LINK = (By.CSS_SELECTOR, "#ui-id-17>span:nth-child(2)")
    MEN_TOPS_JACKETS_LINK = (By.CSS_SELECTOR, "#ui-id-19>span")
    MEN_TOPS_HOODIES_LINK = (By.CSS_SELECTOR, "#ui-id-20>span")
    MEN_TOPS_TEES_LINK = (By.CSS_SELECTOR, "#ui-id-21>span")
    MEN_TOPS_TANKS_LINK = (By.CSS_SELECTOR, "#ui-id-22>span")
    MEN_BOTTOMS_LINK = (By.CSS_SELECTOR, "#ui-id-18>span:nth-child(2)")
    MEN_BOTTOMS_PANTS_LINK = (By.CSS_SELECTOR, "#ui-id-23>span")
    MEN_BOTTOMS_SHORTS_LINK = (By.CSS_SELECTOR, "#ui-id-24>span")
    WHATS_NEW = (By.CSS_SELECTOR, "#ui-id-3>span")
    WOMEN = (By.CSS_SELECTOR, "#ui-id-4>span")
    MEN = (By.CSS_SELECTOR, "#ui-id-5>span")
    GEAR = (By.CSS_SELECTOR, "#ui-id-6>span")
    GEAR_BAGS = (By.CSS_SELECTOR, "#ui-id-25>span")
    GEAR_FITNESS = (By.CSS_SELECTOR, "#ui-id-26>span")
    GEAR_WATCHES = (By.CSS_SELECTOR, "#ui-id-27>span")
    TRAINING = (By.CSS_SELECTOR, "#ui-id-7>span")
    TRAINING_VIDEO = (By.CSS_SELECTOR, "#ui-id-28>span")
    SALE = (By.CSS_SELECTOR, "#ui-id-8>span")
class HomePageLocators():
    SHOP_NEW_YOGA = (By.CSS_SELECTOR,".action.more.button")
    SHOP_PANTS = (By.CSS_SELECTOR,".action.more.icon")
    SHOP_ERIN_RECOMMENDS = (By.CSS_SELECTOR,".home-erin>.content>.action.more.icon")
    SHOP_TEES = (By.CSS_SELECTOR,".home-t-shirts>.content>.action.more.icon")
    SHOP_PERFORMANCE = (By.CSS_SELECTOR,".home-performance>.content>.action.more.icon")
    SHOP_ECO_FRIENDLY = (By.CSS_SELECTOR,".home-eco>.content>.action.more.icon")
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
    SHOW_CART_WINDOW = (By.CSS_SELECTOR, ".showcart")
    VIEW_CART_PAGE = (By.CSS_SELECTOR, ".viewcart>span")

    OLIVIA_NAME = (By.CSS_SELECTOR,"a.product-item-link")
    OLIVIA_SIZE_XS = (By.CSS_SELECTOR,"#option-label-size-143-item-166")
    OLIVIA_SIZE_S = (By.CSS_SELECTOR, "#option-label-size-143-item-167")
    OLIVIA_SIZE_M = (By.CSS_SELECTOR, "#option-label-size-143-item-168")
    OLIVIA_SIZE_L = (By.CSS_SELECTOR, "#option-label-size-143-item-169")
    OLIVIA_SIZE_XL = (By.CSS_SELECTOR, "#option-label-size-143-item-170")
    OLIVIA_COLOR_BLACK = (By.CSS_SELECTOR, "#option-label-color-93-item-49")
    OLIVIA_COLOR_BLUE = (By.CSS_SELECTOR, "#option-label-color-93-item-50")
    OLIVIA_COLOR_PURPLE = (By.CSS_SELECTOR, "#option-label-color-93-item-57")
    BUTTON_ADD_OLIVIA_TO_CART = (By.CSS_SELECTOR, "button.tocart>span")

    JUNO_NAME = (By.CSS_SELECTOR,"li:nth-child(2)  a.product-item-link")
    JUNO_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(2) #option-label-size-143-item-166")
    JUNO_SIZE_S = (By.CSS_SELECTOR,"li:nth-child(2) #option-label-size-143-item-167")
    JUNO_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(2) #option-label-size-143-item-168")
    JUNO_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(2) #option-label-size-143-item-169")
    JUNO_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(2) #option-label-size-143-item-170")
    JUNO_COLOR_BLUE = (By.CSS_SELECTOR, "li:nth-child(2) #option-label-color-93-item-50")
    JUNO_COLOR_GREEN = (By.CSS_SELECTOR,"li:nth-child(2) #option-label-color-93-item-53")
    JUNO_COLOR_PURPLE = (By.CSS_SELECTOR, "li:nth-child(2) #option-label-color-93-item-57")
    BUTTON_ADD_JUNO_TO_CART = (By.CSS_SELECTOR, "li:nth-child(2) .tocart>span")

    NEVE_NAME = (By.CSS_SELECTOR, "li:nth-child(3)  a.product-item-link")
    NEVE_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-size-143-item-166")
    NEVE_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-size-143-item-167")
    NEVE_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-size-143-item-168")
    NEVE_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-size-143-item-169")
    NEVE_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-size-143-item-170")
    NEVE_COLOR_BLACK = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-color-93-item-49")
    NEVE_COLOR_BLUE = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-color-93-item-50")
    NEVE_COLOR_ORANGE = (By.CSS_SELECTOR, "li:nth-child(3) #option-label-color-93-item-56")
    BUTTON_ADD_NEVE_TO_CART = (By.CSS_SELECTOR, "li:nth-child(3) .tocart>span")

    NADIA_NAME = (By.CSS_SELECTOR, "li:nth-child(4)  a.product-item-link")
    NADIA_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-size-143-item-166")
    NADIA_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-size-143-item-167")
    NADIA_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-size-143-item-168")
    NADIA_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-size-143-item-169")
    NADIA_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-size-143-item-170")
    NADIA_COLOR_BLACK = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-color-93-item-49")
    NADIA_COLOR_ORANGE = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-color-93-item-56")
    NADIA_COLOR_YELLOW = (By.CSS_SELECTOR, "li:nth-child(4) #option-label-color-93-item-60")
    BUTTON_ADD_NADIA_TO_CART = (By.CSS_SELECTOR, "li:nth-child(4) .tocart>span")

    JADE_NAME = (By.CSS_SELECTOR, "li:nth-child(5)  a.product-item-link")
    JADE_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-size-143-item-166")
    JADE_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-size-143-item-167")
    JADE_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-size-143-item-168")
    JADE_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-size-143-item-169")
    JADE_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-size-143-item-170")
    JADE_COLOR_BLUE = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-color-93-item-50")
    JADE_COLOR_GRAY = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-color-93-item-52")
    JADE_COLOR_GREEN = (By.CSS_SELECTOR, "li:nth-child(5) #option-label-color-93-item-53")
    BUTTON_ADD_JADE_TO_CART = (By.CSS_SELECTOR, "li:nth-child(5) .tocart>span")

    ADRIENNE_NAME = (By.CSS_SELECTOR, "li:nth-child(6)  a.product-item-link")
    ADRIENNE_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-size-143-item-166")
    ADRIENNE_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-size-143-item-167")
    ADRIENNE_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-size-143-item-168")
    ADRIENNE_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-size-143-item-169")
    ADRIENNE_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-size-143-item-170")
    ADRIENNE_COLOR_GRAY = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-color-93-item-52")
    ADRIENNE_COLOR_ORANGE = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-color-93-item-56")
    ADRIENNE_COLOR_PURPLE = (By.CSS_SELECTOR, "li:nth-child(6) #option-label-color-93-item-57")
    BUTTON_ADD_ADRIENNE_TO_CART = (By.CSS_SELECTOR, "li:nth-child(6) .tocart>span")

    INEZ_NAME = (By.CSS_SELECTOR, "li:nth-child(7)  a.product-item-link")
    INEZ_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-size-143-item-166")
    INEZ_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-size-143-item-167")
    INEZ_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-size-143-item-168")
    INEZ_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-size-143-item-169")
    INEZ_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-size-143-item-170")
    INEZ_COLOR_ORANGE = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-color-93-item-56")
    INEZ_COLOR_PURPLE = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-color-93-item-57")
    INEZ_COLOR_RED = (By.CSS_SELECTOR, "li:nth-child(7) #option-label-color-93-item-58")
    BUTTON_ADD_INEZ_TO_CART = (By.CSS_SELECTOR, "li:nth-child(7) .tocart>span")

    RIONA_NAME = (By.CSS_SELECTOR, "li:nth-child(8)  a.product-item-link")
    RIONA_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-size-143-item-166")
    RIONA_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-size-143-item-167")
    RIONA_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-size-143-item-168")
    RIONA_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-size-143-item-169")
    RIONA_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-size-143-item-170")
    RIONA_COLOR_BROWN = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-color-93-item-51")
    RIONA_COLOR_GREEN = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-color-93-item-53")
    RIONA_COLOR_RED = (By.CSS_SELECTOR, "li:nth-child(8) #option-label-color-93-item-58")
    BUTTON_ADD_RIONA_TO_CART = (By.CSS_SELECTOR, "li:nth-child(8) .tocart>span")

    INGRID_NAME = (By.CSS_SELECTOR, "li:nth-child(9)  a.product-item-link")
    INGRID_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-size-143-item-166")
    INGRID_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-size-143-item-167")
    INGRID_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-size-143-item-168")
    INGRID_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-size-143-item-169")
    INGRID_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-size-143-item-170")
    INGRID_COLOR_ORANGE = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-color-93-item-56")
    INGRID_COLOR_RED = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-color-93-item-58")
    INGRID_COLOR_WHITE = (By.CSS_SELECTOR, "li:nth-child(9) #option-label-color-93-item-59")
    BUTTON_ADD_INGRID_TO_CART = (By.CSS_SELECTOR, "li:nth-child(9) .tocart>span")

    AUGUSTA_NAME = (By.CSS_SELECTOR, "li:nth-child(10)  a.product-item-link")
    AUGUSTA_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-size-143-item-166")
    AUGUSTA_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-size-143-item-167")
    AUGUSTA_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-size-143-item-168")
    AUGUSTA_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-size-143-item-169")
    AUGUSTA_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-size-143-item-170")
    AUGUSTA_COLOR_BLUE = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-color-93-item-50")
    AUGUSTA_COLOR_ORANGE = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-color-93-item-56")
    AUGUSTA_COLOR_RED = (By.CSS_SELECTOR, "li:nth-child(10) #option-label-color-93-item-58")
    BUTTON_ADD_AUGUSTA_TO_CART = (By.CSS_SELECTOR, "li:nth-child(10) .tocart>span")

    JOSIE_NAME = (By.CSS_SELECTOR, "li:nth-child(11)  a.product-item-link")
    JOSIE_SIZE_XS = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-size-143-item-166")
    JOSIE_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-size-143-item-167")
    JOSIE_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-size-143-item-168")
    JOSIE_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-size-143-item-169")
    JOSIE_SIZE_XL = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-size-143-item-170")
    JOSIE_COLOR_BLACK = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-color-93-item-49")
    JOSIE_COLOR_BLUE = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-color-93-item-50")
    JOSIE_COLOR_GRAY = (By.CSS_SELECTOR, "li:nth-child(11) #option-label-color-93-item-52")
    BUTTON_ADD_JOSIE_TO_CART = (By.CSS_SELECTOR, "li:nth-child(11) .tocart>span")

    STELLAR_NAME = (By.CSS_SELECTOR, "li:nth-child(12)  a.product-item-link")
    STELLAR_SIZE_S = (By.CSS_SELECTOR, "li:nth-child(12) #option-label-size-143-item-167")
    STELLAR_SIZE_M = (By.CSS_SELECTOR, "li:nth-child(12) #option-label-size-143-item-168")
    STELLAR_SIZE_L = (By.CSS_SELECTOR, "li:nth-child(12) #option-label-size-143-item-169")
    STELLAR_COLOR_BLUE = (By.CSS_SELECTOR, "li:nth-child(12) #option-label-color-93-item-50")
    STELLAR_COLOR_RED = (By.CSS_SELECTOR, "li:nth-child(12) #option-label-color-93-item-58")
    STELLAR_COLOR_YELLOW = (By.CSS_SELECTOR, "li:nth-child(12) #option-label-color-93-item-60")
    BUTTON_ADD_STELLAR_TO_CART = (By.CSS_SELECTOR, "li:nth-child(12) .tocart>span")


class CartWindowLocators():
    NAME = (By.CSS_SELECTOR,".product-item-name>a")
    Quantity = (By.CSS_SELECTOR,"span.count")
    SEE_DETAILS = (By.CSS_SELECTOR, (".toggle>span"))
    SIZE = (By.CSS_SELECTOR,"dd.values:nth-child(2)")
    COLOR = (By.CSS_SELECTOR,"dd.values:nth-child(4)")
class SuccessfulMessageLOCATORS():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".messages>.message-success>div")
    LINK_TO_CART_FROM_SUCCESS_MESSAGE = (By.CSS_SELECTOR,".messages>.message-success>div>a")
class MenPageLocators():
    MEN_TOPS_LINK_LEFT_BAR = (By.CSS_SELECTOR,"ol>li>a")
    MEN_BOTTOMS_LINK_LEFT_BAR =(By.CSS_SELECTOR,"ol>li:nth-child(2)>a")
    MEN_HOODIES_LINK_LEFT_BAR = (By.CSS_SELECTOR,".categories-menu>ul>li>a")
    MEN_JACKET_LINK_LEFT_BAR= (By.CSS_SELECTOR,".categories-menu>ul>li:nth-child(2)>a")
    MEN_TEES_LINK_LEFT_BAR = (By.CSS_SELECTOR,".categories-menu>ul>li:nth-child(3)>a")
    MEN_TANKS_LINK_LEFT_BAR = (By.CSS_SELECTOR,".categories-menu>ul>li:nth-child(4)>a")
    MEN_PANTS_LINK_LEFT_BAR = (By.CSS_SELECTOR,".categories-menu>ul:nth-child(4)>li>a")
    MEN_SHORTS_LINK_LEFT_BAR = (By.CSS_SELECTOR,".categories-menu>ul:nth-child(4)>li:nth-child(2)>a")
class WomenPageLocators():
    WOMEN_TOPS_LINK_LEFT_BAR = (By.CSS_SELECTOR, "ol>li>a")
    WOMEN_BOTTOMS_LINK_LEFT_BAR = (By.CSS_SELECTOR, "ol>li:nth-child(2)>a")
    WOMEN_HOODIES_LINK_LEFT_BAR = (By.CSS_SELECTOR, ".categories-menu>ul>li>a")
    WOMEN_JACKETS_LINK_LEFT_BAR = (By.CSS_SELECTOR, ".categories-menu>ul>li:nth-child(2)>a")
    WOMEN_TEES_LINK_LEFT_BAR = (By.CSS_SELECTOR, ".categories-menu>ul>li:nth-child(3)>a")
    WOMEN_BRAS_LINK_LEFT_BAR = (By.CSS_SELECTOR, ".categories-menu>ul>li:nth-child(4)>a")
    WOMEN_PANTS_LINK_LEFT_BAR = (By.CSS_SELECTOR, ".categories-menu>ul:nth-child(4)>li>a")
    WOMEN_SHORTS_LINK_LEFT_BAR = (By.CSS_SELECTOR, ".categories-menu>ul:nth-child(4)>li:nth-child(2)>a")

    WOMEN_SHOP_NEW_YOGA_BUTTON = (".content>span.more")
    WOMENS_TEES_LINK =(".content>span.more.icon")
    WOMEN_SHOP_TANKS_LINK = (".content>span.more.icon:nth-child(3)")
    WOMEN_SHOP_ERIN_LINK = ("a.womens-erin>span.content>span.more.icon")
    WOMEN_SHOP_PANTS_LINK = ("a.womens-category-pants>span.content>span.more.icon")
    WOMEN_SHOP_SHORTS_LINK = ("a.womens-category-shorts>span.content>span.more.icon")
    WOMEN_SHOP_NOW_LINK = ("a.womens-category-tanks>span.content>span.more.icon")
    WOMEN_RADIANT_TEE_LINK = (".product-item-link")
    WOMEN_BREATHE_EASY_TANK_LINK = (".product-item-name>a")
    WOMEN_SELENE_YOGA_LINK = (".product-item:nth-child(3) a.product-item-link")
    DEIRDRE_RELAXED_FIT_LINK = (".product-item:nth-child(4) a.product-item-link")
