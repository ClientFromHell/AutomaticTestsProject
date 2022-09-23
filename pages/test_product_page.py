from .product_page import ProductPage
from .locators import ProductPageLocators
import pytest


@pytest.mark.parametrize('promo', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param(
                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo"
                                       "=offer7",
                                       marks=pytest.mark.xfail),
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    url = f'{promo}'
    # url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, url)
    page.open()
    page.add_button_exists()
    page.add_product_to_basket()
    page.the_product_name_is_the_same()
    page.the_price_name_is_the_same()


def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page (browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket_and_check_if_it_is_empty()