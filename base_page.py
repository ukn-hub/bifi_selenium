from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def select_state(self, select_element, state):

        select = Select(select_element)

        select.select_by_visible_text(state)
