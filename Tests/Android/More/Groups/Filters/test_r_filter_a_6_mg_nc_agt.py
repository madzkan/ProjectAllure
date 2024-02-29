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


def test_more_groups_filter_6(driver):

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

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW8'
    # android_widget_imageview8 = driver.find_element(By.XPATH,
    #                                                 "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview8.click()
    click_first_drop = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    click_first_drop.click()

    time.sleep(5)

    # 5. Click 'My Groups'
    my_groups = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'My Groups']")
    my_groups.click()

    time.sleep(5)

    # 6. Click 'Newly Created'
    newly_created = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Newly Created']")
    newly_created.click()

    time.sleep(5)

    # 7. Click 'ANDROID.WIDGET.IMAGEVIEW9'
    # android_widget_imageview9 = driver.find_element(By.XPATH,
    #                                                 "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview9.click()
    close_btn = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    close_btn.click()

    time.sleep(5)

    # 8. Is 'ANDROID.VIEW.VIEWGROUP' is clickable?
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup.is_enabled()