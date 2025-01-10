package com.example;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class TestLineChart {

    private WebDriver driver;

    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "C:/Automation/chromedriver.exe");
        ChromeOptions options = new ChromeOptions();
        driver = new ChromeDriver(options);
        driver.get("https://inerg-test.web.app/");
    }

    @Test
    public void testSelectStateAndPrintChartValues() {
        LineChartPage lineChartPage = new LineChartPage(driver);
        lineChartPage.selectStateAndWaitForChart("Kerala");  // Update with actual state
        lineChartPage.printTextValues();  // Print the text values
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}