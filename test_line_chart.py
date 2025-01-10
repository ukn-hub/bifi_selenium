import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from line_chart_page import LineChartPage

class TestLineChart(unittest.TestCase):

    def setUp(self):
        service = Service('C:/Automation/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://inerg-test.web.app/')

    def test_select_state_and_print_chart_values(self):
        line_chart_page = LineChartPage(self.driver)
        line_chart_page.select_state_and_wait_for_chart('Kerala')  # Update with actual state
        line_chart_page.print_text_values()  # Print the text values

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
