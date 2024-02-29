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


def test_more_groups_featured_image(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(5)

    # 2. Make a Swipe gesture from ('637','1342') to ('646','860')
    driver.swipe(start_x=637, start_y=1342, end_x=646, end_y=860, duration=300)

    time.sleep(3)

    # 3. Click 'Groups'
    groups = driver.find_element(By.XPATH,
                                 "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    groups.click()

    time.sleep(5)

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW'
    android_widget_imageview = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView")
    android_widget_imageview.click()

    time.sleep(5)

    # 5. Does 'Feed' contain 'Feed'?
    feed = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Feed']")
    step_output = feed.text
    assert step_output and ("Feed" in step_output)

    # 6. Does 'Members' contain 'Members'?
    members = driver.find_element(By.XPATH,
                                  "//android.widget.TextView[@text = 'Members']")
    step_output = members.text
    assert step_output and ("Members" in step_output)