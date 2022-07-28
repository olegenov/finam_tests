from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import StrategiesLocators
from ..utils import wait

class StrategiesPage(BasePage):
    @property
    def search_field(self):
        search_field = self.get_element(
            'Search field',
            StrategiesLocators.SEARCH_FIELD
        )

        return search_field

    @property
    def search_button(self):
        search_button = self.get_element(
            'Search button',
            StrategiesLocators.SEARCH_BUTTON
        )

        return search_button

    @property
    @wait(1)
    def search_results(self):
        search_results = self.get_elements(
            'Card title',
            StrategiesLocators.CARD_TITLE
        )

        return search_results

    def should_be_strategies_page(self):
        assert self.driver.current_url == self.url, 'Incorrect url'

    def compare_names(self, seacrh_request, name):
        assert seacrh_request in name, 'Search request doesnt match results\n'\
                                       f'"{seacrh_request}" expected, got {name}'
