from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from math import log, sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, MainPageLocators


class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def add_some_product_to_basket(self):
        add_product = self.browser.find_element(*MainPageLocators.SOME_PRODUCT)
        add_product.click()

    def go_to_basket_and_check_if_it_is_empty(self):
        # self.add_some_product_to_basket() # Uncomment if you want to simulate adding a product
        basket_btn = self.browser.find_element(*MainPageLocators.SEE_BASKET)
        basket_btn.click()
        assert self.is_not_element_present(*MainPageLocators.SOME_PRODUCT_IN_BASKET), "BASKET IS NOT EMPY"
        assert self.is_element_present(*MainPageLocators.EMPTY_BASKET_STATUS),  "NO STATUS THAT THE BASKET IS EMPTY"
