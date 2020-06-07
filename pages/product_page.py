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
        message_expected = product + " has been added to your basket."
        message_actual = self.browser.find_element(*ProductPageLocators.PRODUCT_NOTIFICATION).text
        assert message_expected == message_actual, f"Incorrect product message:{message_actual}\nExpected:{message_expected}"

    def verify_basket_notification(self, price):
        message_expected = "Your basket total is now " + price
        message_actual = self.browser.find_element(*ProductPageLocators.BASKET_NOTIFICATION).text
        assert message_expected == message_actual, f"Incorrect basket message:{message_actual}\nExpected:{message_expected}"

    def verify_item_adding(self, product, price):
        self.verify_product_notification(product)
        self.verify_basket_notification(price)

    def success_message_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NOTIFICATION), "Success message is present! Not expected"

    def success_message_is_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NOTIFICATION), "Success message is present! Expected to dissapear"




