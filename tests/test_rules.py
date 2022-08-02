import allure
import pytest


class TestRules():
    @allure.testcase('#1')
    @allure.feature('Открытие вкладки правил')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_rules_tab(self, app):
        with allure.step('Step 1. Перейти на страницу https://docs.comon.ru/general-information/'):
            app.models.rules.go_to('https://docs.comon.ru/general-information/')

        with allure.step('Step 2. Кликнуть по вкладке "Подключение счета"'):
            app.models.rules.click_tab('Подключение счета')

        with allure.step('Asserts. Проверить соответствие заголовка страницы шагу 2'):
            app.models.rules.compare_title('Подключение счета')
    
    @allure.testcase('#2')
    @allure.feature('Открытие вкладки правил по кнопке')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_next_tab(self, app):
        with allure.step('Step 1. Перейти на страницу https://docs.comon.ru/general-information/multiple-strategies/'):
            app.models.rules.go_to('https://docs.comon.ru/general-information/multiple-strategies/')

        with allure.step('Step 2. Кликнуть по кнопке "Копилка"'):
            app.models.rules.click_next_button()

        with allure.step('Asserts. Проверить соответствие заголовка страницы шагу 2'):
            app.models.rules.compare_title('Копилка')
    
    @allure.testcase('#3')
    @allure.feature('Открытие гиперссылки личного кабинета')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_hyperlink(self, app):
        with allure.step('Step 1. Перейти на страницу https://docs.comon.ru/general-information/'):
            app.models.rules.go_to('https://docs.comon.ru/general-information/')

        with allure.step('Step 2. Кликнуть по вкладке "Регистрация и авторизация"'):
            app.models.rules.click_tab('Регистрация и авторизация')

        with allure.step('Step 3. Кликнуть по гиперссылке "Личного кабинета"'):
            app.models.rules.click_hyperlink('Личного кабинета')
        
        with allure.step('Asserts. Проверить открытие страницы личного кабинета'):
            app.models.rules.compare_url('edox.finam.ru')
    
    @allure.testcase('#4')
    @allure.feature('Поиск раздела "Синхронизация"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_tab(self, app):
        with allure.step('Step 1. Перейти на страницу https://docs.comon.ru/general-information/'):
            app.models.rules.go_to('https://docs.comon.ru/general-information/')

        with allure.step('Step 2. В поле "Поиск" ввводим название раздела и нажимаем на первое совпадение'):
            app.models.rules.search_tab('Синхронизация')
        
        with allure.step('Asserts. Проверить соответствие заголовка страницы шагу 2'):
            app.models.rules.compare_title('Синхронизация')
