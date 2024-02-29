import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from addons.swipe_and_find_element import SwipeAndFindElement
import pytest
import allure


def test_home_groups_send_messages(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Swipe 'Up' to 'Groups - Home'
    # groups_home = (
    #     By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    # driver.addons().execute(
    #     SwipeAndFindElement.verticalswipeandroid(
    #         swipeDirection="Up",
    #         bottomMarginPercent=0,
    #         topMarginPercent=0,
    #         maxSwipes=0,
    #         timeoutMilliseconds=0), *groups_home)

    driver.swipe(start_x=1023, start_y=1183, end_x=945, end_y=466, duration=300)

    # 2. Click 'See all4'
    see_all4 = driver.find_element(By.XPATH,
                                   "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'See all']")
    see_all4.click()

    time.sleep(10)

    # 3. Click 'ANDROID.VIEW.VIEWGROUP13'
    android_view_viewgroup13 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup13.click()

    time.sleep(5)

    # 4. Swipe 'Up' to 'Send Messages - gh'
    # send_messages_gh = (
    #     By.XPATH, "//android.widget.TextView[@text = 'Send Messages']")
    # driver.addons().execute(
    #     SwipeAndFindElement.verticalswipeandroid(
    #         swipeDirection="Up",
    #         bottomMarginPercent=0,
    #         topMarginPercent=0,
    #         maxSwipes=0,
    #         timeoutMilliseconds=0), *send_messages_gh)

    driver.swipe(start_x=1023, start_y=1183, end_x=945, end_y=466, duration=300)

    # 5. Click 'Send Messages - gh'
    send_messages_gh = driver.find_element(By.XPATH,
                                           "//android.widget.TextView[@text = 'Send Messages']")
    send_messages_gh.click()

    time.sleep(5)

    # 6. Does 'Send Messages' contain 'Send Messages'?
    send_messages = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Send Messages']")
    step_output = send_messages.text
    assert step_output and ("Send Messages" in step_output)