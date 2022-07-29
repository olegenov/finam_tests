from selenium.webdriver.common.by import By


class BaseLocators:
    STRATEGY_LINK = (By.CSS_SELECTOR, 'li[data-marker="menu/managers"]')


class StrategiesLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'div[data-marker="searchByName"] input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[data-marker="searchIcon"]')
    CARD_TITLE = (By.CSS_SELECTOR, 'p[data-marker="strategyTitle"]')
    GRAPH = (By.CSS_SELECTOR, 'img.MuiCardMedia-img')

class StrategyLocators:
    TITLE = (By.CSS_SELECTOR, 'h1.MuiTypography-h1')
