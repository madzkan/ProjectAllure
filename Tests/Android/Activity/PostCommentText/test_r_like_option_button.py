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


def test_activity_like_option_button(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    activity = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 1. Click 'ANDROID.WIDGET.IMAGEVIEW27'
    # android_widget_imageview27 = driver.find_element(By.XPATH,   "//android.view.ViewGroup[2]/android.view.ViewGroup[6]/android.widget.ImageView")
    # android_widget_imageview27.click()
    option_ellips = driver.find_element(By.XPATH, "//android.view.ViewGroup[5]/android.widget.TextView[@text = '']")
    option_ellips.click()

    time.sleep(5)

    # 2. Click 'Like'
    like = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Like']")
    like.click()

    time.sleep(5)

    # 3. Click 'ANDROID.WIDGET.IMAGEVIEW27'
    # android_widget_imageview27 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[6]/android.widget.ImageView")
    # android_widget_imageview27.click()
    option_ellips = driver.find_element(By.XPATH,
                                        "//android.view.ViewGroup[5]/android.widget.TextView[@text = '']")
    option_ellips.click()

    time.sleep(5)

    # 4. 'Unlike' contains text '[NONE]'?
    unlike = (By.XPATH, "//android.widget.TextView[@text = 'Unlike']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *unlike)

    # 5. Click 'Unlike'
    unlike = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Unlike']")
    unlike.click()