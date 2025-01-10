from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def select_state(self, select_element, state):
        select = Select(select_element)
        self.wait.until(EC.element_to_be_clickable(select_element))
        select.select_by_visible_text(state)
        print(f"State '{state}' selected in dropdown")