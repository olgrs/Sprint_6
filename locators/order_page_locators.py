from selenium.webdriver.common.by import By


class OrderPageLocators:
    BUTTON_CONFIRM_YES = By.XPATH, "//button[text()='Да']"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
    CHECKBOX_BLACK = By.XPATH, "//input[@id='black']"
    CHECKBOX_GREY = By.XPATH, "//input[@id='grey']"
    DROPDOWN_RENTAL_PERIOD = By.XPATH, "//div[contains(@class, 'Dropdown-root')]"
    FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    FIELD_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    FIELD_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    FIELD_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    METRO_STATION_INPUT = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_STATION_OPTION = By.XPATH, "//button[contains(@class, 'Order_SelectOption') and .//div[text()='{}']]"
    MODAL_CONFIRM = By.XPATH, "//div[contains(@class, 'Order_Modal')]"
    MODAL_SUCCESS_TEXT = By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[text()='Заказ оформлен']"
    MODAL_SUCCESS_ORDER = By.XPATH, "//button[text()='Посмотреть статус']"
    RENTAL_PERIOD_OPTION = By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']"
