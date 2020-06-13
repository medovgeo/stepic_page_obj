from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NOTIFICATION = (By.CSS_SELECTOR, "#messages > div > div")
    BASKET_NOTIFICATION = (By.CSS_SELECTOR, "#messages > .alert-info > div > p")
    PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div > div:nth-child(2) > h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div > div:nth-child(2) > p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = ((By.CSS_SELECTOR, ".btn.btn-default[href$='basket/']"))
    BASKET_ITEM = ((By.CSS_SELECTOR, ".basket-items"))
    BASKET_MESSAGE = ((By.CSS_SELECTOR, "#content_inner > p"))