import allure
import pytest

from locators.main_page_locators import MainPageLocators
from urls import BASE_URL, DZEN_URL
from data_collection import ORDER_DATA_1, ORDER_DATA_2


class TestOrder:
    @allure.title("Проверка текста в окне успешного заказа")
    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_TOP, ORDER_DATA_2),
        ]
    )
    def test_success_message(self, order_page, button_locator, order_data):
        order_page.set_order(button_locator, order_data)
        assert "Заказ оформлен" in order_page.get_success_text(), (
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
    def test_scooter_logo_redirect(self, order_page, main_page, button_locator, order_data):
        order_page.set_order(button_locator, order_data)
        order_page.close_success_modal()
        main_page.click_scooter_logo()
        assert order_page.get_current_url() == BASE_URL, (
            f"После клика на самокат не открылась главная. Текущий URL: {order_page.get_current_url()}"
        )

    @allure.title("Переход на Дзен по логотипу Яндекса после заказа")
    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_TOP, ORDER_DATA_2),
        ]
    )
    def test_yandex_logo_redirect(self, order_page, main_page, button_locator, order_data):
        order_page.set_order(button_locator, order_data)
        order_page.close_success_modal()
        main_page.click_yandex_logo()
        current_url = main_page.get_current_url().split('?')[0]
        assert current_url == DZEN_URL, (
            f"Ожидался переход на главную Дзена, но получен URL: {current_url}"
        )
