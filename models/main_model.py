from .base_model import BaseModel
from ..pages.strategies_page import StrategiesPage


class Main(BaseModel):
    def click_strategies_link(self):
        self.page.strategies_link.click()
        self.page = StrategiesPage(self.driver, self.driver.current_url)
        self.page.should_be_strategies_page()
