from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):
    def go_to_basket_and_check_if_it_is_empty(self):
        # self.add_some_product_to_basket() # Uncomment if you want to simulate adding a product
        basket_btn = self.browser.find_element(*MainPageLocators.SEE_BASKET)
        basket_btn.click()
        assert self.is_not_element_present(*MainPageLocators.SOME_PRODUCT_IN_BASKET), "BASKET IS NOT EMPY"
        assert self.is_element_present(*MainPageLocators.EMPTY_BASKET_STATUS),  "NO STATUS THAT THE BASKET IS EMPTY"

