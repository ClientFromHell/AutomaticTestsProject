from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEE_BASKET = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    EMPTY_BASKET_STATUS = (By.CSS_SELECTOR, '#content_inner>p')
    SOME_PRODUCT = (By.XPATH, "//article/div[2]/form/button")
    SOME_PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket-items")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_AMOUNT = (By.CSS_SELECTOR, ".alert > div > p:nth-child(1) > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
