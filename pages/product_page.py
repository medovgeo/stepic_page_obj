from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text


