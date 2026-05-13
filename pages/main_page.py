import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from urls import BASE_URL
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем главную страницу")
    def open(self):
        """Открывает главную страницу"""
        self.go_to_url(BASE_URL)

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        try:
            cookie_btn = self.driver.find_element("id", "rcc-confirm-button")
            self.driver.execute_script("arguments[0].click();", cookie_btn)
        except Exception:
            pass

    @allure.step("Нажимаем кнопку 'Заказать'")
    def click_order_button(self, button_locator):
        self.click_to_element(button_locator)

    @allure.step("Кликаем по вопросу: {question_text}")
    def click_question_by_text(self, question_text):
        """Кликает по вопросу с указанным текстом"""
        locator = ("xpath", f"//div[contains(@class, 'accordion__button') and text()='{question_text}']")
        element = self.find_element_with_wait(locator)
        self.scroll_to_element(element)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получаем текст ответа для вопроса: {question_text}")
    def get_answer_text(self, question_text):
        """Открывает вопрос и возвращает текст ответа"""
        self.click_question_by_text(question_text)
        panel_locator = ("xpath", f"//div[text()='{question_text}']/ancestor::div[contains(@class, 'accordion__item')]//div[contains(@class, 'accordion__panel')]")
        return self.get_text_from_element(panel_locator)

    @allure.step("Кликаем по логотипу cамоката")
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_to_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Переключаемся на новое окно")
    def switch_to_new_window(self):
        """Переключается на последнее открытое окно и возвращает дескриптор исходного."""
        original = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for handle in self.driver.window_handles:
            if handle != original:
                self.driver.switch_to.window(handle)
                return original
        raise Exception("Новое окно не найдено")

    @allure.step("Переключаемся на окно: {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Закрываем текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Ожидаем, что URL станет равен {url}")
    def wait_for_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Ожидаем, что URL перестанет быть 'about:blank'")
    def wait_for_url_not_blank(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != "about:blank")
        except TimeoutException:
            pass

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url
