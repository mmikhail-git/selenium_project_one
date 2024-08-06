import time
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review
#@pytest.mark.xfail
@pytest.mark.parametrize('language', ["ru"])
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_in_basket()
    page.should_be_equal_cart_and_product_price()

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review
@pytest.mark.parametrize('language', ["ru"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review
@pytest.mark.parametrize('language', ["ru"])
def test_guest_cant_see_success_message(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review
@pytest.mark.parametrize('language', ["ru"])
def test_message_disappeared_after_adding_product_to_basket(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    time.sleep(3)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_goods_in_basket()
    basket_page.should_be_empty_label_in_basket()
    time.sleep(5)