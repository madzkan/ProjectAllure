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


def test_more_courses_category_filter_1(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(7)

    # 2. Swipe 'Up' to 'Course Categories  -more'
    # course_categories_more = (
    #     By.XPATH, "//android.widget.TextView[@text = 'Course Categories']")
    # driver.addons().execute(
    #     SwipeAndFindElement.verticalswipeandroid(
    #         swipeDirection="Up",
    #         bottomMarginPercent=0,
    #         topMarginPercent=0,
    #         maxSwipes=0,
    #         timeoutMilliseconds=0), *course_categories_more)

    # 2. Make a Swipe gesture from ('637','1342') to ('646','860')
    driver.swipe(start_x=637, start_y=1342, end_x=646, end_y=860, duration=300)

    time.sleep(3)

    # 3. Click 'Course Categories  -more'
    course_categories_more = driver.find_element(By.XPATH,
                                                 "//android.widget.TextView[@text = 'Course Categories']")
    course_categories_more.click()

    time.sleep(5)

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW38'
    # android_widget_imageview38 = driver.find_element(By.XPATH,
    #                                                  "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview38.click()
    filter_dd = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
    filter_dd.click()

    time.sleep(5)

    # 5. Click 'Alphabetical'
    alphabetical = driver.find_element(By.XPATH,
                                       "//android.view.ViewGroup[1]/android.widget.TextView[@text = 'Alphabetical']")
    alphabetical.click()

    time.sleep(5)

    # 6. Click 'Alphabetical1'
    alphabetical1 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Alphabetical']")
    alphabetical1.click()

    time.sleep(5)

    # 7. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    close_btn = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
    close_btn.click()