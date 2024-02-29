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


def test_more_courses_filter_6(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(5)

    # 2. Click 'Courses5'
    courses5 = driver.find_element(By.XPATH,
                                   "//android.view.ViewGroup/android.widget.TextView[@text = 'Courses']")
    courses5.click()

    time.sleep(5)

    # 3. Click 'ANDROID.WIDGET.IMAGEVIEW38'
    # android_widget_imageview38 = driver.find_element(By.XPATH,
    #                                                  "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview38.click()
    filter_dd = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
    filter_dd.click()

    time.sleep(5)

    # 4. Click 'My Courses'
    my_courses = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'My Courses']")
    my_courses.click()

    time.sleep(5)

    # 5. Click 'My Progress'
    my_progress = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'My Progress']")
    my_progress.click()

    time.sleep(5)

    # 6. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    close_btn = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
    close_btn.click()

    time.sleep(5)

    # 7. Is 'ANDROID.VIEW.VIEWGROUP13' is clickable?
    android_view_viewgroup13 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup13.is_enabled()