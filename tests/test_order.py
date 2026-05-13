import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL, DZEN_URL
from data_collection import ORDER_DATA_1, ORDER_DATA_2


class TestOrder:
    def _complete_order(self, driver, button_locator, order_data):
        """Успешное оформление заказа"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button(button_locator)

        order_page = OrderPage(driver)
        order_page.fill_first_step(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        order_page.fill_second_step(
            order_data["date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )
        order_page.confirm_order()
        success_text = order_page.get_success_text()
        order_page.close_success_modal()
        return main_page, order_page, success_text

    @allure.title("Проверка текста в окне успешного заказа")
    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_TOP, ORDER_DATA_2),
        ]
    )
    def test_success_message(self, driver, button_locator, order_data):
        _, _, success_text = self._complete_order(driver, button_locator, order_data)
        assert "Заказ оформлен" in success_text, (
            f"Ожидалось 'Заказ оформлен', но получено '{success_text}'"
        )

    @allure.title("Переход на главную по клику на самокат после заказа")
    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_TOP, ORDER_DATA_2),
        ]
    )
    def test_scooter_logo_redirect(self, driver, button_locator, order_data):
        main_page, _, _ = self._complete_order(driver, button_locator, order_data)
        main_page.click_scooter_logo()
        main_page.wait_for_url_to_be(BASE_URL)
        assert main_page.get_current_url() == BASE_URL, (
            f"После клика на самоката не открылась главная. Текущий URL: {main_page.get_current_url()}"
        )

    @allure.title("Переход на Дзен по логотипу Яндекса после заказа")
    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_TOP, ORDER_DATA_2),
        ]
    )
    def test_yandex_logo_redirect(self, driver, button_locator, order_data):
        main_page, _, _ = self._complete_order(driver, button_locator, order_data)
        main_page.click_yandex_logo()

        original_window = main_page.switch_to_new_window()
        if original_window is None:
            assert False, "После клика на логотип Яндекса не открылось новое окно"

        main_page.wait_for_url_not_blank()
        current_url = main_page.get_current_url().split('?')[0]
        assert current_url == DZEN_URL, (
            f"Ожидался переход на главную Дзена, но получен URL: {current_url}"
        )
        main_page.close_current_window()
        main_page.switch_to_window(original_window)
