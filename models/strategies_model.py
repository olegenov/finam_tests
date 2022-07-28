from .base_model import BaseModel


class Strategies(BaseModel):
    def input_partial_name(self, name):
        self.page.search_field.clear()
        self.page.search_field.send_keys(name)
        self.page.search_button.click()

    def compare_partial_search_results(self, name):
        strategies = self.page.search_results

        for strategy_title in strategies:
            self.page.compare_names(name, strategy_title.text)
