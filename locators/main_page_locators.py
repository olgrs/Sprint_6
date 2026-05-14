from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']"
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, "//div[@id='accordion__heading-7']"
    ORDER_BUTTON_BOTTOM = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    ORDER_BUTTON_TOP = By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']"
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
