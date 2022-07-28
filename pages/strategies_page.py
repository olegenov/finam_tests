from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

from .locators import StrategiesLocators


class StrategiesPage(BasePage):
    def search_field(self):
        self.should_be_search_field()
        search_field = self.driver.find_element(
            *StrategiesLocators.SEARCH_FIELD
        )

        return search_field

    def search_button(self):
        self.should_be_search_button()
        search_button = self.driver.find_element(
            *StrategiesLocators.SEARCH_BUTTON
        )

        return search_button

    def search_results(self):
        search_results = self.driver.find_elements(
            *StrategiesLocators.CARD_TITLE
        )

        return search_results

    def should_be_strategies_page(self):
        assert self.driver.current_url == self.url, \
               'Incorrect url'

    def should_be_search_field(self):
        search_field = self.driver.find_element(
            *StrategiesLocators.SEARCH_FIELD
        )

        assert search_field, 'Search field is not found'

    def should_be_search_button(self):
        search_button = self.driver.find_element(
            *StrategiesLocators.SEARCH_BUTTON
        )

        assert search_button, 'Search button is not found'

    def compare_names(self, seacrh_request, name):
        assert seacrh_request in name, \
               'Search request doesnt match results\n' \
               f'"{seacrh_request}" expected, got {name}'
