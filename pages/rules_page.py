from .base_page import BasePage

from .locators import RulesLocators


class RulesPage(BasePage):
    @property
    def title(self):
        return self.get_element(
            'Title',
            RulesLocators.TITLE
        )

    @property
    def next_button(self):
        return self.get_elements(
            'Next button',
            RulesLocators.NEXT_BUTTON
        )[1]

    @property
    def search_field(self):
        return self.get_element(
            'Search field',
            RulesLocators.SEATCH_FIELD
        )

    @property
    def similaritites(self):
        return self.get_elements(
            'Similaritites',
            RulesLocators.SIMILARITIES
        )

    def tab(self, name):
        locator = RulesLocators.TAB
        parsed_locator = (locator[0], locator[1].format(name))

        return self.get_element(
            'Tab',
            parsed_locator
        )

    def hyperlink(self, text):
        locator = RulesLocators.HYPERLINK
        parsed_locator = (locator[0], locator[1].format(text))

        return self.get_element(
            'Hyperlink',
            parsed_locator
        )

    def compare_titles(self, got, expected):
        assert got == expected, 'Title doesnt match request\n'\
                                f'"{expected}" expected, got "{got}"'

    def compare_urls(self, got, expected):
        assert expected in got, 'Url doesnt mach request\n'\
                                f'"{expected}" expected, got "{got}"'
