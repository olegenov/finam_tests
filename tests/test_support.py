import allure
import pytest


class TestClientSupport():
    @allure.testcase('')
    @allure.feature('Открытие окна звонка в "клиентскую поддержку"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_client_support_number(self, app):
        with allure.step('Step 1. Переходим на страницу "Блоги"'):
            app.models.blogs.go_to('https://www.comon.ru/blogs/new/')
        
        with allure.step('Step 2. Прокручиваем до конца страницу'):
            app.models.footer.check_client_support_in_footer()
        
        with allure.step('Step 3. Кликаем по номеру "Клиентская поддержка"'):
            app.models.footer.click_client_support_number()

        with allure.step('Asserts. Проверяем открытие alert'):
            app.models.footer.сheck_opened_alert()

    @allure.testcase('')
    @allure.feature('Открытие окна звонка в службу "голосовой трейдинг"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_voice_trading_window(self, app):
        with allure.step('Step 1. Переходим на страницу "Блоги"'):
            app.models.blogs.go_to('https://www.comon.ru/blogs/new/')
        
        with allure.step('Step 2. Кликаем по пункту "Контакты"'):
            app.models.nav.click_contacts()
        
        with allure.step('Step 3. Кликаем по кнопке "Голосовой трейдинг"'):
            app.models.contact.click_voice_trading()
        
        with allure.step('Asserts. Проверяем открытие диалогового окна'):
            app.models.contact.check_opened_dialog('Голосовой трейдинг')

    @allure.testcase('')
    @allure.feature('Открытие окна звонка в службу "банковские карты"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_bank_cards_window(self, app):
        with allure.step('Step 1. Переходим на страницу "Блоги"'):
            app.models.blogs.go_to('https://www.comon.ru/blogs/new/')
        
        with allure.step('Step 2. Кликаем по пункту "Контакты"'):
            app.models.nav.click_contacts()
        
        with allure.step('Step 3. Кликаем по кнопке "Банковские карты"'):
            app.models.contact.click_bank_cards_support()
        
        with allure.step('Asserts. Проверяем открытие диалогового окна'):
            app.models.contact.check_opened_dialog('Банковские карты')
    
    @allure.testcase('')
    @allure.feature('Открытие окна звонка в службу "контакт-центр"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_client_support_window(self, app):
        with allure.step('Step 1. Переходим на страницу "Блоги"'):
            app.models.blogs.go_to('https://www.comon.ru/blogs/new/')
        
        with allure.step('Step 2. Кликаем по пункту "Контакты"'):
            app.models.nav.click_contacts()
        
        with allure.step('Step 3. Кликаем по кнопке "Клиентская поддержка"'):
            app.models.contact.click_client_support()
        
        with allure.step('Asserts. Проверяем открытие диалогового окна'):
            app.models.contact.check_opened_dialog('Клиентская поддержка')

    @allure.testcase('')
    @allure.feature('Вывод email "службы поддержки"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_open_client_support_email(self, app):
        with allure.step('Step 1. Переходим на страницу "Блоги"'):
            app.models.blogs.go_to('https://www.comon.ru/blogs/new/')
        
        with allure.step('Step 2. Кликаем по пункту "Контакты"'):
            app.models.nav.click_contacts()
        
        with allure.step('Asserts. Проверяем, что email службы поддержки выводится на страницу'):
            app.models.contact.check_client_support_email()
