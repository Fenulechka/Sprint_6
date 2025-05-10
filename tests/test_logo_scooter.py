import allure
import pytest
from locators.order_locacators import OrderLocators
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL

class TestLogoScooter:
    @allure.title("Тест проверки перехода с лого Яндекса на главную странице Дзена в новом окне через редирект")
    def test_logo_scooter(self, driver):
        with allure.step("Открытие страницы заказа"):
            home_page = HomePage(driver)
            home_page.click_on_element(OrderLocators.ORDER_BUTTON_TOP)

        with allure.step("Находим и кликаем на логотип Самоката"):
            home_page.click_logo_scooter()

        with allure.step("Ждем загрузки страницы и проверяем URL"):
            WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL))

        with allure.step("Проверяем, что открылась главная страница Самоката"):
            assert "https://qa-scooter.praktikum-services.ru" in driver.current_url