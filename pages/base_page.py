from .locators import BaseLocators

class BasePage():
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url

    def strategies_link(self):
        self.should_be_strategies_link()
        strategies_link = self.driver.find_element(
            *BaseLocators.STRATEGY_LINK
        )
        
        return strategies_link

    def should_be_strategies_link(self):
        assert self.driver.find_element(*BaseLocators.STRATEGY_LINK), \
               'Strategy link is not found'
