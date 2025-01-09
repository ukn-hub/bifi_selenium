from selenium.webdriver.common.by import By
from base_page import BasePage


class LineChartPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

        self.state_dropdown = driver.find_element(By.ID, 'stateDropdown')  # Update with actual ID

        self.chart_points = driver.find_elements(By.CSS_SELECTOR, '.chart-point')  # Update with actual selector


    def print_chart_values(self):

        for point in self.chart_points:

            print(point.text)
