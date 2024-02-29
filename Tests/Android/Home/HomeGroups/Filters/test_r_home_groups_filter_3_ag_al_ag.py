import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from addons.swipe_and_find_element import SwipeAndFindElement
import pytest
import allure


def test_homegroups_id_filter_3(driver):

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

    # 3. Click 'ANDROID.WIDGET.IMAGEVIEW38'
    # android_widget_imageview38 = driver.find_element(By.XPATH,
    #                                                  "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview38.click()
    open_filter = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = '']")
    open_filter.click()

    time.sleep(5)

    # 4. Click 'Alphabetical4'
    alphabetical4 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Alphabetical']")
    alphabetical4.click()

    time.sleep(5)

    # 5. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    close_btn = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
    close_btn.click()

    time.sleep(5)

    # 6. Does 'Alphabetical5' contain 'Alphabetical'?
    alphabetical5 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Alphabetical']")
    step_output = alphabetical5.text
    assert step_output and ("Alphabetical" in step_output)