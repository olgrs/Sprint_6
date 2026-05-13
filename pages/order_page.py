import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполняем первый шаг заказа")
    def fill_first_step(self, name, surname, address, metro_station, phone):
        """Заполняет поля первого шага и нажимает Далее"""
        self.add_text_to_element(OrderPageLocators.FIELD_NAME, name)
        self.add_text_to_element(OrderPageLocators.FIELD_SURNAME, surname)
        self.add_text_to_element(OrderPageLocators.FIELD_ADDRESS, address)
        self.click_to_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_to_element(
            self.format_locators(OrderPageLocators.METRO_STATION_OPTION,
                                 metro_station)
        )
        self.add_text_to_element(OrderPageLocators.FIELD_PHONE, phone)

        try:
            self.click_to_element(OrderPageLocators.BUTTON_NEXT)
        except:
            next_btn = self.driver.find_element(*OrderPageLocators.BUTTON_NEXT)
            self.driver.execute_script("arguments[0].click();", next_btn)

    @allure.step("Заполняем второй шаг заказа")
    def fill_second_step(self, date, rental_period, color, comment=""):
        """Заполняет поля второго шага и нажимает Заказать"""
        date_field = self.find_element_with_wait(OrderPageLocators.FIELD_DATE)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ESCAPE)
        self.click_to_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        self.click_to_element(
            self.format_locators(OrderPageLocators.RENTAL_PERIOD_OPTION, rental_period)
        )
        if color == "black":
            self.click_to_element(OrderPageLocators.CHECKBOX_BLACK)
        elif color == "grey":
            self.click_to_element(OrderPageLocators.CHECKBOX_GREY)
        if comment:
            self.add_text_to_element(OrderPageLocators.FIELD_COMMENT, comment)

        try:
            self.click_to_element(OrderPageLocators.BUTTON_ORDER)
        except:
            order_btn = self.driver.find_element(*OrderPageLocators.BUTTON_ORDER)
            self.driver.execute_script("arguments[0].click();", order_btn)

    @allure.step("Подтверждаем заказ в модальном окне")
    def confirm_order(self):
        """Подтверждает заказ в модальном окне"""
        self.find_element_with_wait(OrderPageLocators.MODAL_CONFIRM)
        self.click_to_element(OrderPageLocators.BUTTON_CONFIRM_YES)

    @allure.step("Получаем текст из окна успеха")
    def get_success_text(self):
        """Возвращает текст из окна успешного заказа"""
        return self.get_text_from_element(OrderPageLocators.MODAL_SUCCESS_TEXT)
    
    @allure.step("Переходим на страницу заказа")
    def close_success_modal(self):
        """Закрывает окно успешного заказа, кликая по кнопке 'Посмотреть статус'"""
        self.click_to_element(OrderPageLocators.MODAL_SUCCESS_ORDER)
