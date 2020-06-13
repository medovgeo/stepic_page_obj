from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div > div:nth-child(2) > h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div > div:nth-child(2) > p")


class BasketPageLocators(object):
    PRODUCT_NOTIFICATION = (By.CSS_SELECTOR, "#messages > div > div")
    BASKET_NOTIFICATION = (By.CSS_SELECTOR, "#messages > .alert-info > div > p")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = ((By.CSS_SELECTOR, ".btn.btn-default[href$='basket/']"))
    BASKET_ITEM = ((By.CSS_SELECTOR, ".basket-items"))
    BASKET_MESSAGE = ((By.CSS_SELECTOR, "#content_inner > p"))
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
