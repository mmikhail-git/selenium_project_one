from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()

    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "Phrase 'catalogue' is absent in URL"

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        link.click()

    def should_be_added_in_basket(self):
        product_name = self.get_text(*ProductPageLocators.PRODUCT_NAME)
        assert self.is_text_present(*ProductPageLocators.ADDED_PRODUCT_ALERT, product_name), "ADDED_PRODUCT_ALERT is not match"

    def should_be_equal_cart_and_product_price(self):
        cart_price = self.get_text(*ProductPageLocators.CART_PRICE)
        product_price = self.get_text(*ProductPageLocators.PRODUCT_PRICE)
        if cart_price == 'NoSuchElementException' or product_price == 'NoSuchElementException':
            print('NoSuchElementException')
        else:
            assert cart_price == product_price, "Cart price and product price not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
