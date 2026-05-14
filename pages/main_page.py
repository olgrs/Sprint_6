import allure

from locators.main_page_locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик по вопросу")
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step("Получение ответа на вопрос")
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Проверяем ответ")
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step("Кликаем по логотипу самоката")
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.find_element_with_wait(MainPageLocators.LOGO_SCOOTER)
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.find_element_with_wait(MainPageLocators.LOGO_YANDEX)
        self.click_to_element(MainPageLocators.LOGO_YANDEX)
        self.switch_to_another_window()
        self.wait_for_url_not_blank()
