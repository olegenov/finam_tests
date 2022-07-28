import time

from .models.main_model import Main
from .models.strategies_model import Strategies

from .pages.main_page import MainPage
from .pages.strategies_page import StrategiesPage


class Models:
    def __init__(self, driver, base_url):
        self.main = Main(driver, MainPage(driver, base_url))
        self.strategies = Strategies(driver, StrategiesPage(driver, base_url))
