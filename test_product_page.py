from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
from mimesis import Person

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10) if no != 7]


@pytest.mark.need_review
@pytest.mark.parametrize('link', urls + [pytest.param(product_base_link + '/?promo=offer7', marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product = page.product_name()
    price = page.product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.verify_item_adding(product, price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.success_message_is_not_present()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.success_message_is_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.success_message_is_dissapeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()
    page.basket_message_is_present()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        user = Person()
        email = user.email()
        password = user.password(length=9)
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.success_message_is_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        product = page.product_name()
        price = page.product_price()
        page.add_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.verify_item_adding(product, price)
