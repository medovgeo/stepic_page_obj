from pages.product_page import ProductPage
import pytest
from time import sleep

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10) if no != 7]


@pytest.mark.parametrize('link', urls + [pytest.param(product_base_link + '/?promo=offer7', marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product = page.product_name()
    price = page.product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # sleep(90)
    page.verify_item_adding(product, price)

