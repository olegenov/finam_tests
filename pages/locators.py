from selenium.webdriver.common.by import By


class BaseLocators:
    STRATEGY_LINK = (By.CSS_SELECTOR, 'li[data-marker="menu/managers"]')
    CONTACT_LINK = (By.CSS_SELECTOR, 'li[data-marker="menu/contact"]')
    CLIENT_SUPPORT = (By.XPATH, '//p[text()="Клиентская поддержка"]')
    CLIENT_SUPPORT_NUMBER = (By.XPATH, '//p[text()="Клиентская поддержка"]/../..//li[2]')


class StrategiesLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'div[data-marker="searchByName"] input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[data-marker="searchIcon"]')
    CARD_TITLE = (By.CSS_SELECTOR, 'p[data-marker="strategyTitle"]')
    GRAPH = (By.CSS_SELECTOR, 'img.MuiCardMedia-img')


class StrategyLocators:
    TITLE = (By.CSS_SELECTOR, 'h1.MuiTypography-h1')


class ContactLocators:
    VOICE_TRADING = (By.CSS_SELECTOR, 'button[data-marker="contactPage/trading"]')
    BANK_CARDS = (By.CSS_SELECTOR, 'button[data-marker="contactPage/cards"]')
    CLIENT_SUPPORT = (By.CSS_SELECTOR, 'button[data-marker="contactPage/contactCenter"]')
    DIALOG = (By.CSS_SELECTOR, 'div[role="dialog"] h2')
    SUPPORT_EMAIL = (By.XPATH, '//a[@data-marker="contactPage/support"]/../p/a')


class RulesLocators:
    TITLE = (By.XPATH, '//h1')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'span.MuiButton-label')
    TAB = (By.XPATH, '//li[@role="treeitem"]//a[text()="{}"]')
    HYPERLINK = (By.XPATH, '//a[text()="{}"]')
    SEATCH_FIELD = (By.CSS_SELECTOR, 'input[value]')
    SIMILARITIES = (By.XPATH, '//ul/a')
