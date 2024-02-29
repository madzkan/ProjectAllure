import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
import pytest
import allure


def test_more_blog(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(10)

    # 2. Click 'Blog'
    blog = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Blog']")
    blog.click()


    # 3. Does 'Blog1' contain 'Blog'?
    # blog1 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Blog']")
    # step_output = blog1.text
    # assert step_output and ("Blog" in step_output)

