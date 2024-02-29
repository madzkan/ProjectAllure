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


def test_more_groups_filter_1(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(5)

    # 2. Swipe 'Up' to 'Groups - More'
    # groups_more = (
    #     By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    # driver.addons().execute(
    #     SwipeAndFindElement.verticalswipeandroid(
    #         swipeDirection="Up",
    #         bottomMarginPercent=0,
    #         topMarginPercent=0,
    #         maxSwipes=1,
    #         timeoutMilliseconds=0), *groups_more)

    # 2. Make a Swipe gesture from ('637','1342') to ('646','860')
    driver.swipe(start_x=637, start_y=1342, end_x=646, end_y=860, duration=300)

    time.sleep(5)

    # 3. Click 'Groups2'
    groups2 = driver.find_element(By.XPATH,
                                  "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    groups2.click()

    time.sleep(5)

    # 4. Does 'All Groups' contain 'All Groups'?
    all_groups = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'All Groups']")
    step_output = all_groups.text
    assert step_output and ("All Groups" in step_output)

    time.sleep(5)

    # 5. Does 'Recently Active' contain 'Recently Active'?
    recently_active = driver.find_element(By.XPATH,
                                          "//android.widget.TextView[@text = 'Recently Active']")
    step_output = recently_active.text
    assert step_output and ("Recently Active" in step_output)

    # 6. Is 'ANDROID.VIEW.VIEWGROUP' is clickable?
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup.is_enabled()