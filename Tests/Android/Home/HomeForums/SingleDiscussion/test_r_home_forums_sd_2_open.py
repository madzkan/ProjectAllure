import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
import pytest
import allure


def test_homeforums_id_filter_2b(driver):

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

    # 2. Click 'ANDROID.VIEW.VIEWGROUP'
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup.click()

    time.sleep(5)

    # 3. Click 'ANDROID.VIEW.VIEWGROUP1'
    android_view_viewgroup1 = driver.find_element(By.XPATH,
                                                  "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup1.click()

    time.sleep(5)

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW5'
    # android_widget_imageview5 = driver.find_element(By.XPATH,
    #                                                 "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView")
    # android_widget_imageview5.click()
    click_ellipsis = driver.find_element(By.XPATH,
                                         "//android.view.ViewGroup[2]/android.widget.TextView[@text = '']")
    click_ellipsis.click()

    time.sleep(5)

    # 5. Click 'Open'
    open = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Open']")
    open.click()