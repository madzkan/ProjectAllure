import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from addons.swipe_and_find_element import SwipeAndFindElement
import pytest
import allure


def test_homeforums_id_filter_2(driver):

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

    driver.swipe(start_x=1023, start_y=1183, end_x=945, end_y=366, duration=300)

    # 2. Click 'See all4'
    see_all4 = driver.find_element(By.XPATH,
                                   "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'See all']")
    see_all4.click()

    time.sleep(10)

    # 3. Click 'All Groups'
    all_groups = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'All Groups']")
    all_groups.click()

    time.sleep(5)

    # 4. Click 'My Groups'
    my_groups = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'My Groups']")
    my_groups.click()

    time.sleep(5)

    # 5. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    close_btn = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    close_btn.click()

    time.sleep(5)

    # 6. Click 'Recently Active'
    recently_active = driver.find_element(By.XPATH,
                                          "//android.widget.TextView[@text = 'Recently Active']")
    recently_active.click()

    time.sleep(5)

    # 7. Click 'Most Members2'
    most_members2 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Most Members']")
    most_members2.click()

    time.sleep(5)

    # 8. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    close_btn = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    close_btn.click()

    time.sleep(5)

    # 9. Is 'ANDROID.VIEW.VIEWGROUP13' is clickable?
    android_view_viewgroup13 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup13.is_enabled()