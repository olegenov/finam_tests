import allure
import pytest


class TestStrategySearch():
    @allure.testcase('')
    @allure.feature('Поиск по неполному названию стратегии')
    @allure.title('Проверить корректность поиска стратегии ' \
                  'по её неполному названию')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_strategy_partial_name_search(self, app):
        folder_url = ''
        partial_name = 'Долгосрочные'

        with allure.step('Step 1. Кликнуть на вкладку "Торговые стратегии"'):
            app.go_to('https://www.comon.ru/')
            app.models.main.click_strategies_link()

        with allure.step('Step 2. В поле "Поиск стратегии" вводим неполное ' \
                        'название стратегии и кликаем по значку поиска'):
            app.models.strategies.input_partial_name(partial_name)

        with allure.step('Asserts. Проверяем, что название стратегии ' \
                        'соответствует шагу 2'):
            app.models.strategies.compare_partial_search_results(partial_name)
