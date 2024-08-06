
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Phrase 'login' is absent in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_reg = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_FORM)
        email_reg.send_keys(email)

        pass1_reg = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTER_FORM)
        pass1_reg.send_keys(password)

        pass2_reg = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTER_FORM)
        pass2_reg.send_keys(password)

        button_reg = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_FORM)
        button_reg.click()

