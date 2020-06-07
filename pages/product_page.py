from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()


    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def verify_product_notification(self, product):
        assert product in self.browser.find_element(*ProductPageLocators.PRODUCT_NOTIFICATION).text, "Product is not present in the message"

    def verify_basket_notification(self, price):
        assert price in self.browser.find_element(*ProductPageLocators.BASKET_NOTIFICATION).text, f"Product is not considered in the basket price"

    def verify_item_adding(self, product, price):
        self.verify_product_notification(product)
        self.verify_basket_notification(price)
