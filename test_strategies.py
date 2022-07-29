import allure
import pytest


class TestStrategySearch():
    @allure.testcase('')
    @allure.feature('Поиск по неполному названию стратегии')
    @allure.title('Проверить корректность поиска стратегии по её неполному названию')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_strategy_partial_name_search(self, app):
        partial_name = 'Долгосрочные'

        with allure.step('Step 1. Кликнуть на вкладку "Торговые стратегии"'):
            app.models.main.click_strategies_link()

        with allure.step('Step 2. В поле "Поиск стратегии" вводим неполное название стратегии и кликаем по значку поиска'):
            app.models.strategies.input_search_request(partial_name)

        with allure.step('Asserts. Проверяем, что название стратегии соответствует шагу 2'):
            app.models.strategies.compare_partial_search_results(partial_name)

    @allure.testcase('')
    @allure.feature('Поиск стратегии по никнейму автора')
    @allure.title('Проверить корректность поиска стратегии по никнейму её автора')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_strategy_author_nickname_search(self, app):
        nickname = 'bsk'

        with allure.step('Step 1. Кликнуть на вкладку "Торговые стратегии"'):
            app.models.main.click_strategies_link()

        with allure.step('Step 2. В поле "Поиск стратегии" вводим никнейм автора стратегии'):
            app.models.strategies.input_search_request(nickname)

        with allure.step('Asserts. Проверяем, что название стратегии соответствует шагу 2'):
            app.models.strategies.compare_search_results_author(nickname)

    @allure.testcase('')
    @allure.feature('Поиск стратегии по ключевому слову')
    @allure.title('Проверить корректность работы поиска')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_strategy_key_word_search(self, app):
        key_name = 'Долгосрочный'

        with allure.step('Step 1. Перейти на страницу https://www.comon.ru/'):
            app.models.main.go_to('https://www.comon.ru/')

        with allure.step('Step 2. Кликнуть по разделу "Стратегии"'):
            app.models.main.click_strategies_link()

        with allure.step('Step 3. В поисковое поле ввести ключ. слово и кликнуть на кнопку поиска'):
            app.models.strategies.input_search_request(key_name)

        with allure.step('Asserts. Проверяем, что название или автор стратегии соответствуют шагу 3'):
            app.models.strategies.compare_key_search_results(key_name)


class TestStrategyCard():
    @allure.testcase('')
    @allure.feature('Переход в карточку стратегии при клике по графику')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_strategy_graph_click(self, app):
        with allure.step('Step 1. Перейдём в https://www.comon.ru/strategies'):
            app.models.strategies.go_to('https://www.comon.ru/strategies')

        with allure.step('Asserts. Нажимаем на график первой стратегии из каталога'):
            app.models.strategies.click_graph()
