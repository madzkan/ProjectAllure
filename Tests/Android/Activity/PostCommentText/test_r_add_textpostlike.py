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


def test_activity_add_textpostlike(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # # 2. 'News Feed' contains text '[NONE]'?
    # news_feed = (By.XPATH, "//android.widget.TextView[@text = 'News Feed']")
    # driver.addons().execute(
    #     VisibleElementsOperations.containstextifvisibleandroid(
    #         text="",
    #         timeout=""), *news_feed)
    #
    # # 3. Is 'ANDROID.WIDGET.IMAGEVIEW20' clickable?
    # android_widget_imageview20 = (
    #     By.XPATH,
    #     "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # driver.addons().execute(
    #     VisibleElementsOperations.isclickableandroid(
    #         timeout=""), *android_widget_imageview20)

    # # 1. Click 'Activity'
    # activity = driver.find_element(By.XPATH,
    #                                "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click 'ANDROID.WIDGET.IMAGEVIEW8'
    # android_widget_imageview8 = driver.find_element(By.XPATH,
    #                                                 "//android.view.ViewGroup[4]/android.widget.ImageView")
    # android_widget_imageview8.click()
    # 2. Click ''
    _ = driver.find_element(By.XPATH,
                            "//android.view.ViewGroup[3]/android.widget.TextView[@text = '']")
    _.click()

    time.sleep(5)

    # 3. Does '1' contain '1'?
    _1 = driver.find_element(By.XPATH,
                             "//android.widget.TextView[@text = '1']")
    step_output = _1.text
    assert step_output and ("1" in step_output)

