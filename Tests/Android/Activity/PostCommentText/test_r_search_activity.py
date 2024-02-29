import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from addons.swipe_and_find_element import SwipeAndFindElement
from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.actions import Actions
from src.testproject.sdk import drivers, addons
import pytest
import allure


def test_activity_search(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    time.sleep(5)

    # 3. Type 'Search' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("Search")

    time.sleep(5)

    # 4. Does 'No Activities found' contain 'No Activities found'?
    no_activities_found = driver.find_element(By.XPATH,
                                              "//android.widget.TextView[@text = 'No Activities found']")
    step_output = no_activities_found.text
    assert step_output and ("No Activities found" in step_output)