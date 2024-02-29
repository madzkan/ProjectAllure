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


def test_activity_privacy_option_button(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click '1'
    _1 = driver.find_element(By.XPATH, "//android.view.ViewGroup[6]/android.widget.TextView[@text = '']")
    _1.click()

    time.sleep(5)

    # 3. Click 'Change Privacy'
    change_privacy = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Change Privacy']")
    change_privacy.click()

    time.sleep(5)

    # 4. Does 'Visibility' contain 'Visibility'?
    visibility = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'Visibility']")
    step_output = visibility.text
    assert step_output and ("Visibility" in step_output)