from .base_model import BaseModel


class Footer(BaseModel):
    def check_client_support_in_footer(self):
        self.page.client_support

    def click_client_support_number(self):
        self.page.client_support_number.click()
    
    def сheck_opened_alert(self):
        self.page.check_support_number_alert()
