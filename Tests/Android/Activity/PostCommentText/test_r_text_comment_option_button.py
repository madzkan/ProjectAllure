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

    # 2. Click 'ANDROID.WIDGET.IMAGEVIEW27'
    android_widget_imageview27 = driver.find_element(By.XPATH,
                                                     "//android.view.ViewGroup[6]/android.widget.TextView[@text = '']")
    android_widget_imageview27.click()

    time.sleep(5)

    # 3. Click 'Comment'
    comment = driver.find_element(By.XPATH,
                                  "//android.widget.TextView[@text = 'Comment']")
    comment.click()

    time.sleep(5)

    # 4. Click 'Type comment...'
    type_comment_ = driver.find_element(By.XPATH,
                                        "//android.widget.EditText[@text = 'Type comment...']")
    type_comment_.click()

    time.sleep(3)

    driver.press_keycode(29)
    driver.press_keycode(30)
    driver.press_keycode(31)

    # 5. Click 'Post'
    post = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Post']")
    post.click()