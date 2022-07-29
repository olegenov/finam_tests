import time

from .models.main_model import Main
from .models.strategies_model import Strategies
from .models.strategy_model import Strategy

from .pages.main_page import MainPage
from .pages.strategies_page import StrategiesPage
from .pages.strategy_page import StrategyPage


class Models:
    def __init__(self, driver, base_url):
        self.main = Main(driver, MainPage(driver, base_url))
        self.strategies = Strategies(driver, StrategiesPage(driver, base_url))
        self.strategy = Strategy(driver, StrategyPage(driver, base_url))
