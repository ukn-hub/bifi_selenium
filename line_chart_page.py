from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage
import time

class LineChartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 30)  # Increased wait time
        try:
            self.state_dropdown = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.data-filter-input'))  # Updated with actual selector
            )
            print("State dropdown found")
        except TimeoutException:
            print("State dropdown not found")
            raise

    def select_state_and_wait_for_chart(self, state):
        try:
            self.select_state(self.state_dropdown, state)
            print(f"State '{state}' selected")
            # Wait for the chart points to load after selecting the state
            self.chart_points = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.graph-representation .points'))  # Updated with actual selector
            )
            print("Chart points found")
        except TimeoutException:
            print("Chart points not found")
            raise

    def print_text_values(self):
        try:
            action = ActionChains(self.driver)
            for point in self.chart_points:
                action.move_to_element(point).perform()
                time.sleep(1)  # Wait for the text to appear
                # Directly get the text content using the locator
                tooltip_elements = self.driver.find_elements(By.CSS_SELECTOR, 'g.hoverlayer g.hovertext text')
                for tooltip_element in tooltip_elements:
                    text_content = tooltip_element.text
                    if text_content:
                        print(text_content)
                    else:
                        print("No text found")
        except TimeoutException:
            print("Text elements not found")
            raise
