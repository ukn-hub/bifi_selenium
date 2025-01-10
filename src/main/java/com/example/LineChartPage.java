package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.util.List;

public class LineChartPage extends BasePage {

    private WebElement stateDropdown;
    private List<WebElement> chartPoints;

    public LineChartPage(WebDriver driver) {
        super(driver);
        try {
            stateDropdown = wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector(".data-filter-input")));
            System.out.println("State dropdown found");
        } catch (TimeoutException e) {
            System.out.println("State dropdown not found");
            throw e;
        }
    }

    public void selectStateAndWaitForChart(String state) {
        try {
            selectState(stateDropdown, state);
            System.out.println("State '" + state + "' selected");
            chartPoints = wait.until(ExpectedConditions.presenceOfAllElementsLocatedBy(By.cssSelector(".graph-representation .points")));
            System.out.println("Chart points found");
        } catch (TimeoutException e) {
            System.out.println("Chart points not found");
            throw e;
        }
    }

    public void printTextValues() {
        try {
            Actions action = new Actions(driver);
            for (WebElement point : chartPoints) {
                action.moveToElement(point).perform();
                Thread.sleep(1000);  // Wait for the text to appear
                List<WebElement> tooltipElements = driver.findElements(By.cssSelector("g.hoverlayer g.hovertext text"));
                for (WebElement tooltipElement : tooltipElements) {
                    String textContent = tooltipElement.getText();
                    if (!textContent.isEmpty()) {
                        System.out.println(textContent);
                    } else {
                        System.out.println("No text found");
                    }
                }
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (TimeoutException e) {
            System.out.println("Text elements not found");
            throw e;
        }
    }
}