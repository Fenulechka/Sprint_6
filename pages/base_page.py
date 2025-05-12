import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.cookie_banner_locator import CookieBannerLocator

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принять куки")
    def accept_cookies(self):
        accept_button = self.driver.find_element(*CookieBannerLocator.COOKIE_BANNER)  # Найти кнопку принятия cookies
        accept_button.click()  # Нажать на кнопку

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать загрузки страницы и проверить URL")
    def wait_for_url(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(locator))

    @allure.step("Базовый метод поиска элемента с ожиданием")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def input_text(self, locator, text):
        element = self.find_element(locator)  # Уже содержит распаковку
        element.clear()
        element.send_keys(text)

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))

    @allure.step("Вернуть текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Вернуть handle текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Подождать открытие нового окна")
    def wait_for_new_window_opened(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, main_window):
        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)
                break