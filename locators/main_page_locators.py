from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
    ORDER_BUTTON_BOTTOM = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    ORDER_BUTTON_TOP = By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']"
