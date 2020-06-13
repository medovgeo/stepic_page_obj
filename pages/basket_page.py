from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def verify_product_notification(self, product):
        message_expected = product + " has been added to your basket."
        message_actual = self.browser.find_element(*BasketPageLocators.PRODUCT_NOTIFICATION).text
        assert message_expected == message_actual, f"Incorrect product message:{message_actual}\nExpected:{message_expected}"

    def verify_basket_notification(self, price):
        message_expected = "Your basket total is now " + price
        message_actual = self.browser.find_element(*BasketPageLocators.BASKET_NOTIFICATION).text
        assert message_expected == message_actual, f"Incorrect basket message:{message_actual}\nExpected:{message_expected}"

    def verify_item_adding(self, product, price):
        self.verify_product_notification(product)
        self.verify_basket_notification(price)

    def success_message_is_not_present(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_NOTIFICATION), "Success message is present! Not expected"

    def success_message_is_dissapeared(self):
        assert self.is_disappeared(
            *BasketPageLocators.PRODUCT_NOTIFICATION), "Success message is present! Expected to dissapear"
