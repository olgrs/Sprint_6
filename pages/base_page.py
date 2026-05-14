from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, some):
        self.wait.until(EC.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def wait_text(self, locator, text):
        self.wait.until_not(
            EC.text_to_be_present_in_element_value(locator, text))
        self.driver.find_element(*locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def switch_to_another_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_not_blank(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")

    def close_cookie_window(self, locator):
        self.find_element_with_wait(locator)
        self.click_to_element(locator)
