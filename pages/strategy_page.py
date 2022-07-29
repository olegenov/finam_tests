from .base_page import BasePage
from .locators import StrategyLocators


class StrategyPage(BasePage):
    @property
    def title(self):
        title = self.get_element(
            'title',
            StrategyLocators.TITLE
        )

        return title

    def compare_titles(self, expected, got):
        assert expected == got, 'Title doesnt match results\n'\
                                f'"{expected}" expected, got {got}'
