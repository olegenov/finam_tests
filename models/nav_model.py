from .base_model import BaseModel

from ..pages.strategies_page import StrategiesPage
from ..pages.contact_page import ContactPage


class Nav(BaseModel):
    def click_strategies_link(self):
        self.page.strategies_link.click()
        self.page = StrategiesPage(self.driver, self.driver.current_url)
        self.page.should_be_right_page('https://www.comon.ru/strategies/?page=1')

    def click_contacts(self):
        self.page.contact_link.click()
        self.page = ContactPage(self.driver, self.driver.current_url)
        self.page.should_be_right_page('https://www.comon.ru/contact/')
