from .base_page import BasePage

from .locators import ContactLocators
from ..utils import wait


class ContactPage(BasePage):
    @property
    def voice_trading(self):
        button = self.get_element(
            'Voice Trading button',
            ContactLocators.VOICE_TRADING
        )

        return button
    
    @property
    def bank_cards(self):
        button = self.get_element(
            'Bank cards button',
            ContactLocators.BANK_CARDS
        )

        return button

    @property
    def client_support(self):
        button = self.get_element(
            'Client support button',
            ContactLocators.CLIENT_SUPPORT
        )

        return button

    @property
    def dialog(self):
        dialog = self.get_element(
            'Dialog',
            ContactLocators.DIALOG
        )

        return dialog

    @property
    def client_support_email(self):
        email = self.get_element(
            'Support email',
            ContactLocators.SUPPORT_EMAIL
        )

        return email

    @wait
    def check_dialog(self, text):
        dialog = self.dialog

        assert dialog.text == text, f'{text} dialog is not present'
