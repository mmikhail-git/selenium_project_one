from selenium.webdriver.common.by import By


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")
    BASKET_ITEM_WRAPPER = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_LABEL = (By.CSS_SELECTOR, "#content_inner > p")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER_FORM = (By.NAME, "registration_submit")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description")
    ADDED_PRODUCT_ALERT = (By.CSS_SELECTOR, ".alertinner strong")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
