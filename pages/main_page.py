import allure
from selenium.common.exceptions import TimeoutException

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
        except TimeoutException:
            pass

    @allure.step("Нажимаем верхнюю кнопку «Заказать»")
    def click_top_order_button(self):
        self.click_to_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажимаем нижнюю кнопку «Заказать»")
    def click_bottom_order_button(self):
        self.click_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

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

    @allure.step("Кликаем по логотипу Самоката")
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_to_element(MainPageLocators.LOGO_YANDEX)
