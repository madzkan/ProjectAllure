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


def test_more_groups_single_tabs_discussion_6(driver):

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
    groups = driver.find_element(By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    groups.click()

    time.sleep(5)

    # 4. Click 'ANDROID.VIEW.VIEWGROUP'
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup.click()

    time.sleep(5)

    # 5. Make a Swipe gesture from ('426','2006') to ('458','1482')
    driver.swipe(start_x=426, start_y=2006,
                 end_x=458, end_y=1482, duration=300)

    time.sleep(10)

    # 6. Click 'Discussions'
    discussions = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'Discussions']")
    discussions.click()

    time.sleep(5)

    # 7. Click '1'
    _1 = driver.find_element(By.XPATH,
                             "//android.view.ViewGroup[1]/android.widget.TextView[@text = '']")
    _1.click()

    time.sleep(5)

    # 8. Does 'Every man's work, whether it be liter...' contain 'Every man's work, whether it be literature, or music or pictures or architecture or anything else, is always a portrait of himself.'?
    every_man_s_work_whether_it_be_liter_ = driver.find_element(By.XPATH,
                                                                "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = concat('Every man', \"'\", 's work, whether it be literature, or music or pictures or architecture or anything else, is always a portrait of himself.')]")
    step_output = every_man_s_work_whether_it_be_liter_.text
    assert step_output and (
            "Every man's work, whether it be literature, or music or pictures or architecture or anything else, is always a portrait of himself." in step_output)