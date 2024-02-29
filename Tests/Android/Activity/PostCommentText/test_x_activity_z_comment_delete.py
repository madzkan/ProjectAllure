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


def test_activity_option_button(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click '3'
    _3 = driver.find_element(By.XPATH,
                             "//android.view.ViewGroup[2]/android.widget.TextView[@text = '']")
    _3.click()

    time.sleep(5)

    # 3. Click 'Delete'
    delete = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Delete']")
    delete.click()

    time.sleep(5)

    # 4. Click 'CONFIRM'
    confirm = driver.find_element(By.ID,
                                  "android:id/button1")
    confirm.click()