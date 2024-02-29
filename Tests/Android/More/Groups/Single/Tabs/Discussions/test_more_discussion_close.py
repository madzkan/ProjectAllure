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


def test_more_groups_single_tabs_discussion_1(driver):

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

    time.sleep(5)

    # 3. Click 'Groups'
    groups = driver.find_element(By.XPATH,
                                 "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    groups.click()

    time.sleep(5)

    # 4. Click 'ANDROID.VIEW.VIEWGROUP'
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup.click()

    time.sleep(10)

    # 5. Make a Swipe gesture from ('426','2006') to ('458','1482')
    driver.swipe(start_x=426, start_y=2006, end_x=458, end_y=1482, duration=300)

    # 6. Click 'Discussions'
    discussions = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Discussions']")
    discussions.click()

    time.sleep(5)

    # 7. Click 'ANDROID.VIEW.VIEWGROUP1'
    # click top discussion
    android_view_viewgroup1 = driver.find_element(By.XPATH,
                                                  "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup1.click()

    time.sleep(5)

    # 8. Click '2'
    _2 = driver.find_element(By.XPATH,
                             "//android.view.ViewGroup[2]/android.widget.TextView[@text = '']")
    _2.click()

    time.sleep(5)

    # 9. Click 'Close'
    close = driver.find_element(By.XPATH,
                                "//android.widget.TextView[@text = 'Close']")
    close.click()