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


def test_more_courses(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(10)

    # 2. Click 'Courses5'
    courses5 = driver.find_element(By.XPATH,
                                   "//android.view.ViewGroup/android.widget.TextView[@text = 'Courses']")
    courses5.click()

    time.sleep(7)

    # 3. Does 'Courses1' contain 'Courses'?
    courses1 = driver.find_element(By.XPATH,
                                   "//android.view.ViewGroup/android.widget.TextView[@text = 'Courses']")
    step_output = courses1.text
    assert step_output and ("Courses" in step_output)

    time.sleep(5)

    # 4. Is 'ANDROID.VIEW.VIEWGROUP13' is clickable?
    android_view_viewgroup13 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup13.is_enabled()