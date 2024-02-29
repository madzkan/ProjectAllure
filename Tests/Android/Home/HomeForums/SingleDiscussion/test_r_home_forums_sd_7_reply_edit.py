import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
import pytest
import allure


def test_homeforums_id_filter_7(driver):

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

    # 3. Click 'ANDROID.VIEW.VIEWGROUP14'
    android_view_viewgroup14 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup14.click()

    time.sleep(5)

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW36'
    # android_widget_imageview36 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.ImageView")
    # android_widget_imageview36.click()
    ellipsise_single_discussion = driver.find_element(By.XPATH,
                                                      "//android.view.ViewGroup[2]/android.widget.TextView[@text = '']")
    ellipsise_single_discussion.click()

    time.sleep(5)

    # 5. Click 'Edit1'
    edit1 = driver.find_element(By.XPATH,
                                "//android.widget.TextView[@text = 'Edit']")
    edit1.click()

    time.sleep(5)

    # 6. Does 'New Reply' contain 'New Reply'?
    new_reply = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'New Reply']")
    step_output = new_reply.text
    assert step_output and ("New Reply" in step_output)