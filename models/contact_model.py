from .base_model import BaseModel

class Contact(BaseModel):
    def click_voice_trading(self):
        self.page.voice_trading.click()
        self.page.check_dialog('Голосовой трейдинг')

    def click_bank_cards_support(self):
        self.page.bank_cards.click()
        self.page.check_dialog('Банковские карты')
    
    def click_client_support(self):
        self.page.client_support.click()
        self.page.check_dialog('Контакт-центр')

    def check_client_support_email(self):
        self.page.client_support_email