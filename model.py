import time

from .models.main_model import Main
from .models.strategies_model import Strategies
from .models.strategy_model import Strategy
from .models.blogs_model import Blogs
from .models.contact_model import Contact
from .models.nav_model import Nav
from .models.footer_model import Footer
from .models.rules_model import Rules

from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.strategies_page import StrategiesPage
from .pages.strategy_page import StrategyPage
from .pages.blogs_page import BlogsPage
from .pages.contact_page import ContactPage
from .pages.rules_page import RulesPage


class Models:
    def __init__(self, driver, base_url):
        self.main = Main(driver, MainPage(driver, base_url))
        self.strategies = Strategies(driver, StrategiesPage(driver, base_url))
        self.strategy = Strategy(driver, StrategyPage(driver, base_url))
        self.blogs = Blogs(driver, BlogsPage(driver, base_url))
        self.contact = Contact(driver, ContactPage(driver, base_url))
        self.nav = Nav(driver, BasePage(driver, base_url))
        self.footer = Footer(driver, BasePage(driver, base_url))
        self.rules = Rules(driver, RulesPage(driver, base_url))
