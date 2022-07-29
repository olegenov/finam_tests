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
    
    @property
    def card_graph(self):
        graph = self.get_element(
            'Graph',
            StrategiesLocators.GRAPH
        )

        return graph
    
    @property
    def card_title(self):
        card_title = self.get_element(
            'Card title',
            StrategiesLocators.CARD_TITLE
        )

        return card_title

    def compare_names(self, expected, got):
        assert expected in got, 'Search request doesnt match results\n'\
                                f'"{expected}" expected, got {got}'

    def name_in_list(self, name, expected_list):
        assert name in expected_list, 'Search request doesnt match results\n'\
                                      f'"{name}" didnt expected'
    
    def key_word_in_result(self, key_word, name, expected_list):
        assert (key_word in name or name in expected_list), 'Search request doesnt match results\n'\
                                      f'"{name}" didnt expected'
