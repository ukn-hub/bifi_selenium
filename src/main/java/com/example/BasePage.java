package com.example;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class BasePage {
    protected WebDriver driver;
    protected WebDriverWait wait;

    public BasePage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, 40);
    }

    public void selectState(WebElement selectElement, String state) {
        Select select = new Select(selectElement);
        wait.until(ExpectedConditions.elementToBeClickable(selectElement));
        select.selectByVisibleText(state);
        System.out.println("State '" + state + "' selected in dropdown");
    }
}