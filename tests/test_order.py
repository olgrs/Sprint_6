import allure
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import BASE_URL, DZEN_URL


ORDER_DATA = [
    (
        "top",
        "Иван",
        "Иванов",
        "ул. Иванова, 1",
        "Бульвар Рокоссовского",
        "89001234567",
        "15.05.2026",
        "сутки",
        "black",
        ""
    ),
    (
        "bottom",
        "Алексей",
        "Алексеев",
        "ул. Алексеева, д.10",
        "Лихоборы",
        "88888888888",
        "12.06.2026",
        "семеро суток",
        "grey",
        "Позвонить за час"
    )
]


class TestOrder:
    @allure.title("Заказ самоката через {button_type} кнопку")
    @pytest.mark.parametrize(
        [
            "button_type",
            "name",
            "surname",
            "address",
            "metro",
            "phone",
            "date",
            "rental_period",
            "color",
            "comment"
        ],
        ORDER_DATA
    )
    @allure.description(
        "Проверка полного позитивного сценария заказа самоката"
    )
    def test_order_success(
        self, driver, button_type, name, surname, address,
        metro, phone, date, rental_period, color, comment
    ):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        if button_type == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page = OrderPage(driver)
        order_page.fill_first_step(name, surname, address, metro, phone)
        order_page.fill_second_step(date, rental_period, color, comment)

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
