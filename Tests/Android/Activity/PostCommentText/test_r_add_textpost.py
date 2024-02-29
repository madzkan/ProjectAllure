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


def test_activity_add_textpost(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click 'ANDROID.WIDGET.IMAGEVIEW10'
    # android_widget_imageview10 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview10.click()
    # 2. Click ''
    pen_click = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
    pen_click.click()

    time.sleep(5)

    # 3. Click 'Write here or use @ to mention someone.'
    write_here_or_use_to_mention_someone_ = driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Write here or use @ to mention someone.']")
    write_here_or_use_to_mention_someone_.click()

    time.sleep(2)

    driver.press_keycode(29)
    driver.press_keycode(30)

    time.sleep(2)

    # 4. Click 'Post'
    post = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Post']")
    post.click()

