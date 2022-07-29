from .base_model import BaseModel
from ..pages.strategy_page import StrategyPage


class Strategies(BaseModel):
    def input_search_request(self, name):
        self.page.search_field.clear()
        self.page.search_field.send_keys(name)
        self.page.search_button.click()

    def compare_partial_search_results(self, name):
        strategies = self.page.search_results

        for strategy_title in strategies:
            self.page.compare_names(name, strategy_title.text)

    def compare_search_results_author(self, name):
        strategies = self.page.search_results

        expected_strategies = [
            'Пан или пропал',
            'Сверхагрессивная',
            'Трендо-Флэтовая',
            'Трендо-Флэтовая Умеренная',
        ]

        for strategy_title in strategies:
            self.page.name_in_list(strategy_title.text, expected_strategies)

    def compare_key_search_results(self, key_word):
        strategies = self.page.search_results
        expected_strategies = [
            'Среднесрочное инвестирование 4 кв. 2021',
        ]

        for strategy_title in strategies:
            self.page.key_word_in_result(
                key_word,
                strategy_title.text,
                expected_strategies
            )

    def click_graph(self):
        card_title = self.page.card_title.text
        self.page.card_graph.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.page = StrategyPage(self.driver, self.driver.current_url)
        page_title = self.page.title.text
        self.page.compare_titles(card_title, page_title)
