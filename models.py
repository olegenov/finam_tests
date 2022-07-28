import time

from selenium import webdriver

from .pages.main_page import MainPage
from .pages.strategies_page import StrategiesPage


class Models:
    def __init__(self, driver, base_url):
        self.main = Main(driver, MainPage(driver, base_url))
        self.strategies = Strategies(driver, StrategiesPage(driver, base_url))


class BaseModel:
    def __init__(self, driver, page):
        self.driver = driver
        self.page = page

    def click_strategies_link(self):
        self.page.strategies_link().click()
        self.page = StrategiesPage(self.driver, self.driver.current_url)
        self.page.should_be_strategies_page()


class Main(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
    

class Strategies(BaseModel):
    def input_partial_name(self, name):
        self.page.search_field().clear()
        self.page.search_field().send_keys(name)
        self.page.search_button().click()
        time.sleep(1)
    
    def compare_partial_search_results(self, name):
        strategies = self.page.search_results()

        for strategy_title in strategies:
            self.page.compare_names(name, strategy_title.text)
