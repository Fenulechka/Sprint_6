import allure
import pytest
from locators.order_locacators import OrderLocators
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogoYandex:
    @allure.title("Тест проверки перехода с лого Яндекса на главную странице Дзена в новом окне через редирект")
    def test_yandex_logo_redirect(self, driver):
        with allure.step("Открытие страницы заказа"):
            home_page = HomePage(driver)
            home_page.click_on_element(OrderLocators.ORDER_BUTTON_TOP)

        with allure.step("Запоминаем текущее окно"):
            main_window = driver.current_window_handle

        with allure.step("Находим и кликаем на логотип Яндекса"):
            home_page.click_logo_yandex()

        with allure.step("Ждем открытия нового окна"):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        with allure.step("Переключаемся на новое окно"):
            for window_handle in driver.window_handles:
                if window_handle != main_window:
                    driver.switch_to.window(window_handle)
                    break

        with allure.step("Ждем загрузки страницы и проверяем URL"):
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))

        with allure.step("Проверяем, что открылась страница Дзена"):
            assert "dzen.ru" in driver.current_url
