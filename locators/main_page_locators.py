from selenium.webdriver.common.by import By


class MainPageLocators:
    BOTTOM_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
    TOP_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']"
