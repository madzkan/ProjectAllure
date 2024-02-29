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


def test_more_profile_pic(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    # 2. Click 'ANDROID.WIDGET.IMAGEVIEW7'
    android_widget_imageview7 = driver.find_element(By.XPATH,
                                                    "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    android_widget_imageview7.click()

    # 3. Does 'Profile' contain 'Profile'?
    profile = driver.find_element(By.XPATH,
                                  "//android.widget.TextView[@text = 'Profile']")
    step_output = profile.text
    assert step_output and ("Profile" in step_output)

    # 4. Does 'Timeline' contain 'Timeline'?
    timeline = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Timeline']")
    step_output = timeline.text
    assert step_output and ("Timeline" in step_output)