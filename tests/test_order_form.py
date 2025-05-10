import allure
import pytest
from locators.order_locacators import OrderLocators
from locators.cookie_banner_locator import CookieBannerLocator
from pages.order_page import OrderPage
from data import UsersTestData

class TestOrderForm:
    @allure.title("Тест формы заказа самоката")
    @pytest.mark.parametrize("start_button,test_data",
                             [(OrderLocators.ORDER_BUTTON_TOP, UsersTestData.SET_1),
                              (OrderLocators.ORDER_BUTTON_BOTTOM, UsersTestData.SET_2)])
    def test_order_form(self, driver, start_button, test_data):
        order_page = OrderPage(driver) # Инициализация страницы
        accept_button = driver.find_element(*CookieBannerLocator.COOKIE_BANNER) # Найти кнопку принятия cookies
        accept_button.click() # Нажать на кнопку
        order_page.click_on_element(start_button)
        order_page.fill_first_order_form(test_data)
        order_page.fill_second_order_form(test_data["order"])
        confirmation_text = order_page.is_order_successful()
        assert 'Заказ оформлен' in confirmation_text, f"Ожидался текст 'Заказ оформлен', но получили: {confirmation_text}"
