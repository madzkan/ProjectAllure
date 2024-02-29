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


def test_activity_add_textcomment(driver):

    driver.reset()
    time.sleep(10)

    login_admin_loop(driver)

    time.sleep(5)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click 'ANDROID.WIDGET.IMAGEVIEW24'
    android_widget_imageview24 = driver.find_element(By.XPATH, "//android.view.ViewGroup[2]/android.view.ViewGroup[5]/android.widget.TextView[@text = '']")
    android_widget_imageview24.click()

    time.sleep(8)

    addcomment = driver.find_element(By.XPATH, "//android.widget.EditText[@text = 'Type comment...']")
    addcomment.click()

    time.sleep(3)

    driver.press_keycode(29)
    driver.press_keycode(30)

    time.sleep(3)

    # 3. Click 'Post'
    post = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Post']")
    post.click()

