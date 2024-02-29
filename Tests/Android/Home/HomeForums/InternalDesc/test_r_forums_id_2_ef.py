import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
import pytest
import allure


def test_homeforums_id_filter_2(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'See all4'
    # see_all4 = driver.find_element(By.XPATH,"//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'See all']")
    # see_all4.click()
    # see_all_forums = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Forums']/following::android.widget.TextView[@text = 'See all']")
    # see_all_forums.click()

    see_all_forums = driver.find_element(By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView")
    see_all_forums.click()

    time.sleep(10)

    # 2. Click 'ANDROID.VIEW.VIEWGROUP13'
    android_view_viewgroup13 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup13.click()

    time.sleep(5)

    # 3. Click 'ANDROID.WIDGET.IMAGEVIEW32'
    # android_widget_imageview32 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview32.click()
    click_enter = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    click_enter.click()

    time.sleep(5)

    # 4. Click 'Feed'
    feed = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Feed']")
    feed.click()

    time.sleep(5)

    # 5. Does 'Feed1' contain 'Feed'?
    feed1 = driver.find_element(By.XPATH,
                                "//android.widget.TextView[@text = 'Feed']")
    step_output = feed1.text
    assert step_output and ("Feed" in step_output)