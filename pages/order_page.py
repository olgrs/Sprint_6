import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from .base_page import BasePage
from urls import BASE_URL


class OrderPage(BasePage):
    @allure.step("Заполняем первый шаг заказа")
    def fill_first_step(self, data):
        """Заполняет поля первого шага"""
        self.add_text_to_element(OrderPageLocators.FIELD_NAME, data["name"])
        self.add_text_to_element(OrderPageLocators.FIELD_SURNAME, data["surname"])
        self.add_text_to_element(OrderPageLocators.FIELD_ADDRESS, data["address"])
        self.click_to_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_to_element(
            self.format_locators(OrderPageLocators.METRO_STATION_OPTION,
                                 data["metro"])
        )
        self.add_text_to_element(OrderPageLocators.FIELD_PHONE, data["phone"])

    @allure.step("Кликаем по кнопке 'Далее'")
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполняем второй шаг заказа")
    def fill_second_step(self, data):
        """Заполняет поля второго шага и нажимает Заказать"""
        date_field = self.find_element_with_wait(OrderPageLocators.FIELD_DATE)
        date_field.send_keys(data["date"])
        date_field.send_keys(Keys.ESCAPE)
        self.click_to_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        self.click_to_element(
            self.format_locators(OrderPageLocators.RENTAL_PERIOD_OPTION, data["rental_period"])
        )
        checkbox_locator = self.format_locators(OrderPageLocators.CHECKBOX_COLOR, data["color"])
        self.click_to_element(checkbox_locator)
        self.add_text_to_element(OrderPageLocators.FIELD_COMMENT, data["comment"])

    @allure.step("Кликаем кнопку 'Заказать' после заполнения данных")
    def click_status_check_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Подтверждаем заказ в модальном окне")
    def confirm_order(self):
        """Подтверждает заказ в модальном окне"""
        self.find_element_with_wait(OrderPageLocators.MODAL_CONFIRM)
        self.click_to_element(OrderPageLocators.BUTTON_CONFIRM_YES)

    @allure.step("Полный цикл заполнения заказа")
    def set_order(self, button_locator, data):
        """Принимает словарь с данными для заказа и выполняет все шаги до подтверждения"""
        self.go_to_url(BASE_URL)
        self.close_cookie_window(BasePageLocators.ACCEPT_COOKIE_BUTTON)
        self.scroll_to_element(button_locator)
        self.click_to_element(button_locator)
        self.fill_first_step(data)
        self.click_next_button()
        self.fill_second_step(data)
        self.click_status_check_button()
        self.confirm_order()

    @allure.step("Получаем текст из окна успеха")
    def get_success_text(self):
        """Возвращает текст из окна успешного заказа"""
        return self.get_text_from_element(OrderPageLocators.MODAL_SUCCESS_TEXT)
    
    @allure.step("Переходим на страницу заказа")
    def close_success_modal(self):
        """Закрывает окно успешного заказа, кликая по кнопке 'Посмотреть статус'"""
        self.scroll_to_element(OrderPageLocators.MODAL_SUCCESS_ORDER)
        self.click_to_element(OrderPageLocators.MODAL_SUCCESS_ORDER)
