import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from line_chart_page import LineChartPage


class TestLineChart(unittest.TestCase):

    def setUp(self):

        # Specify the path to the ChromeDriver executable

        service = Service('C:/Automation/UI_Mathew/hqe0-efficiency-utilities-dev (1)/chromedriver.exe')

        self.driver = webdriver.Chrome(service=service)

        self.driver.get('https://inerg-test.web.app/')

 

    def test_select_state_and_print_chart_values(self):

        line_chart_page = LineChartPage(self.driver)

        line_chart_page.select_state(line_chart_page.state_dropdown, 'California')  # Update with actual state

        line_chart_page.print_chart_values()

 

    def tearDown(self):

        self.driver.quit()

 

if __name__ == '__main__':

    unittest.main()
