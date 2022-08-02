from .base_model import BaseModel


class Contact(BaseModel):
    def click_voice_trading(self):
        self.page.voice_trading.click()

    def click_bank_cards_support(self):
        self.page.bank_cards.click()
    
    def click_client_support(self):
        self.page.client_support.click()

    def check_client_support_email(self):
        self.page.client_support_email

    def check_opened_dialog(self, name):
        self.page.check_dialog(name)
