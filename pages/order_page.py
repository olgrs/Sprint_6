import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage:
    BUTTON_CONFIRM_YES = "//button[text()='Да']"
    BUTTON_NEXT = "//button[text()='Далее']"
    BUTTON_ORDER = "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
    CHECKBOX_BLACK = "//input[@id='black']"
    CHECKBOX_GREY = "//input[@id='grey']"
    DROPDOWN_RENTAL_PERIOD = "//div[contains(@class, 'Dropdown-root')]"
    FIELD_ADDRESS = "//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_COMMENT = "//input[@placeholder='Комментарий для курьера']"
    FIELD_DATE = "//input[@placeholder='* Когда привезти самокат']"
    FIELD_NAME = "//input[@placeholder='* Имя']"
    FIELD_PHONE = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    FIELD_SURNAME = "//input[@placeholder='* Фамилия']"
    METRO_STATION_INPUT = "//input[@placeholder='* Станция метро']"
    METRO_STATION_OPTION = "//button[contains(@class, 'Order_SelectOption') and .//div[text()='{}']]"
    MODAL_CONFIRM = "//div[contains(@class, 'Order_Modal')]"
    MODAL_SUCCESS_TEXT = "//div[contains(@class, 'Order_Modal')]//div[text()='Заказ оформлен']"
    MODAL_SUCCESS_VIEW = "//button[text()='Посмотреть статус']"
    RENTAL_PERIOD_OPTION = "//div[contains(@class, 'Dropdown-option') and text()='{}']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполняем первый шаг заказа")
    def fill_first_step(self, name, surname, address, metro_station, phone):
        """Заполняет поля первого шага и нажимает Далее"""
        self.wait.until(EC.visibility_of_element_located(("xpath", self.FIELD_NAME))).send_keys(name)
        self.driver.find_element("xpath", self.FIELD_SURNAME).send_keys(surname)
        self.driver.find_element("xpath", self.FIELD_ADDRESS).send_keys(address)
        self.driver.find_element("xpath", self.METRO_STATION_INPUT).click()
        self.wait.until(EC.element_to_be_clickable(("xpath", self.METRO_STATION_OPTION.format(metro_station)))).click()
        self.driver.find_element("xpath", self.FIELD_PHONE).send_keys(phone)
        next_button = self.driver.find_element("xpath", self.BUTTON_NEXT)
        try:
            next_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", next_button)

    @allure.step("Заполняем второй шаг заказа")
    def fill_second_step(self, date, rental_period, color, comment=""):
        """Заполняет поля второго шага и нажимает Заказать"""
        date_field = self.wait.until(EC.visibility_of_element_located(("xpath", self.FIELD_DATE)))
        date_field.send_keys(date)
        date_field.send_keys(Keys.ESCAPE)
        dropdown = self.driver.find_element("xpath", self.DROPDOWN_RENTAL_PERIOD)
        try:
            dropdown.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", dropdown)

        self.wait.until(EC.element_to_be_clickable(("xpath", self.RENTAL_PERIOD_OPTION.format(rental_period)))).click()
        if color == "black":
            self.driver.find_element("xpath", self.CHECKBOX_BLACK).click()
        elif color == "grey":
            self.driver.find_element("xpath", self.CHECKBOX_GREY).click()
        if comment:
            self.driver.find_element("xpath", self.FIELD_COMMENT).send_keys(comment)
        order_btn = self.driver.find_element("xpath", self.BUTTON_ORDER)
        try:
            order_btn.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", order_btn)

    @allure.step("Подтверждаем заказ в модальном окне")
    def confirm_order(self):
        """Подтверждает заказ в модальном окне"""
        self.wait.until(EC.visibility_of_element_located(("xpath", self.MODAL_CONFIRM)))
        self.wait.until(EC.element_to_be_clickable(("xpath", self.BUTTON_CONFIRM_YES))).click()

    @allure.step("Получаем текст из окна успеха")
    def get_success_text(self):
        """Возвращает текст из окна успешного заказа"""
        return self.wait.until(EC.visibility_of_element_located(("xpath", self.MODAL_SUCCESS_TEXT))).text
    
    @allure.step("Переходим на страницу заказа")
    def close_success_modal(self):
        """Закрывает окно успешного заказа, кликая по кнопке 'Посмотреть статус'"""
        btn = self.wait.until(EC.element_to_be_clickable(("xpath", self.MODAL_SUCCESS_VIEW)))
        btn.click()
