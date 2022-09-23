from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    PRODUCT_PRICE = ''
    PRODUCT_NAME = ''

    def add_button_exists(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), 'ADDBASKET BUTTON DOES NOT EXIST'

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.the_price_name_is_the_same()

    def the_product_name_is_the_same(self):
        self.PRODUCT_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.PRODUCT_NAME == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text, \
            "PRODUCTS NAME DOES NOT MATCH "
        print(f"{self.PRODUCT_NAME} is correct product name")

    def the_price_name_is_the_same(self):
        self.PRODUCT_PRICE = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        assert float(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]) == \
               float(self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT).text[1:]), \
            "PRICE IS NOT THE SAME"
        print(f"{self.PRODUCT_PRICE} is correct product price")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
