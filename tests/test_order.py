import allure
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL, DZEN_URL
from data_collection import ORDER_DATA_1, ORDER_DATA_2


class TestOrder:
    @allure.title("Заказ самоката")
    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_BOTTOM,
             ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_TOP,
             ORDER_DATA_2),
        ]
    )
    @allure.description(
        "Проверка полного позитивного сценария заказа самоката"
    )
    def test_order_create(
        self, driver, button_locator, order_data
    ):
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
        assert "Заказ оформлен" in success_text, (
            f"Ожидалось 'Заказ оформлен', но получено '{success_text}'"
        )

        order_page.close_success_modal()

        main_page.click_scooter_logo()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL, (
            "После клика на самокат не произошел переход на главную."
            f"Текущий URL: {driver.current_url}"
        )

        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [
            wh for wh in driver.window_handles
            if wh != original_window
        ][0]
        driver.switch_to.window(new_window)

        try:
            WebDriverWait(driver, 10).until(
                lambda d: d.current_url != "about:blank"
            )
        except TimeoutException:
            pass

        current_url = driver.current_url.split('?')[0]
        assert current_url == DZEN_URL, (
            f"Ожидался переход на главную страницу Дзена, "
            f"но получен URL: {current_url}"
        )

        driver.close()
        driver.switch_to.window(original_window)
