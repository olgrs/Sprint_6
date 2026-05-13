import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
