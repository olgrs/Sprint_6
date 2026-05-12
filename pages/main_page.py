import allure
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    URL = "https://qa-scooter.education-services.ru/"

    BOTTOM_ORDER_BUTTON = "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    LOGO_SCOOTER = "//a[contains(@class, 'Header_LogoScooter')]"
    LOGO_YANDEX = "//a[contains(@class, 'Header_LogoYandex')]"
    TOP_ORDER_BUTTON = "//div[contains(@class, 'Header')]/button[text()='Заказать']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем главную страницу")
    def open(self):
        """Открывает главную страницу"""
        self.driver.get(self.URL)


    def is_cookie_panel_present(self):
        """Проверяет наличие панели куки"""
        return len(self.driver.find_elements("id", "rcc-confirm-button")) > 0

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        """Закрывает панель куки, если она есть"""
        if self.is_cookie_panel_present():
            btn = self.driver.find_element("id", "rcc-confirm-button")
            self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Нажимаем верхнюю кнопку «Заказать»")
    def click_top_order_button(self):
        """Клик по верхней кнопке Заказать"""
        self.wait.until(EC.element_to_be_clickable(
            ("xpath", self.TOP_ORDER_BUTTON)
        )).click()

    @allure.step("Нажимаем нижнюю кнопку «Заказать»")
    def click_bottom_order_button(self):
        """Клик по нижней кнопке Заказать"""
        self.wait.until(EC.element_to_be_clickable(
            ("xpath", self.BOTTOM_ORDER_BUTTON)
        )).click()

    @allure.step("Кликаем по вопросу: {question_text}")
    def click_question_by_text(self, question_text):
        """Кликает по вопросу с указанным текстом"""
        locator = ("xpath", f"//div[contains(@class, 'accordion__button') and text()='{question_text}']")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получаем текст ответа для вопроса: {question_text}")
    def get_answer_text(self, question_text):
        """Открывает вопрос и возвращает текст ответа"""
        self.click_question_by_text(question_text)
        panel_locator = ("xpath", f"//div[text()='{question_text}']/ancestor::div[contains(@class, 'accordion__item')]//div[contains(@class, 'accordion__panel')]")
        panel = self.wait.until(EC.visibility_of_element_located(panel_locator))
        return panel.text

    @allure.step("Кликаем по логотипу Самоката")
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.wait.until(EC.element_to_be_clickable(("xpath", self.LOGO_SCOOTER))).click()

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.wait.until(EC.element_to_be_clickable(("xpath", self.LOGO_YANDEX))).click()
