from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .locators import BaseLocators


class BasePage():
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url

    def should_be_right_page(self, url):
        assert self.driver.current_url == url, f'Incorrect url\n{url} expected, {self.driver.current_url} got'

    @property
    def strategies_link(self):
        strategies_link = self.get_element(
            'Strategy link',
            BaseLocators.STRATEGY_LINK
        )
        
        return strategies_link

    def get_element(self, element, selector, wait=1):
        if self.is_visibility_of_element(selector, wait):
            return self.driver.find_element(*selector)
        else:
            raise TimeoutError(f'{element} is not found')

    def get_elements(self, element, selector):
        try: 
            return self.driver.find_elements(*selector)
        except:
            raise f'{element} are not found'
    
    def is_visibility_of_element(self, selector, wait):
        try:
            WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutError:
            return False
        
        return True
