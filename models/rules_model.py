from .base_model import BaseModel


class Rules(BaseModel):
    def click_tab(self, name):
        self.page.tab(name).click()

    def compare_title(self, expected):
        got = self.page.title.text
        self.page.compare_titles(got, expected)

    def click_next_button(self):
        self.page.next_button.click()

    def click_hyperlink(self, text):
        self.page.hyperlink(text).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def search_tab(self, name):
        self.page.search_field.clear()
        self.page.search_field.send_keys(name)
        self.page.similaritites[0].click()

    def compare_url(self, expected):
        got = self.driver.current_url
        self.page.compare_urls(got, expected)
