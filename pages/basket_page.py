from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators, BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, \
            "Phrase 'basket' is absent in URL"

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_WRAPPER), \
           "Goods is presented, but should not be"

    def should_be_empty_label_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_LABEL), \
            "Empty label is not presented"
