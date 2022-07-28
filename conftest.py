import pytest

from selenium import webdriver

from .apps import Application


@pytest.fixture(scope="function")
def app():
    print("\nRunning app..")
    base_url = 'https://www.comon.ru'
    app = Application(webdriver.Chrome(), base_url)

    yield app

    print("\nQuiting browser..")
    app.driver.quit()
