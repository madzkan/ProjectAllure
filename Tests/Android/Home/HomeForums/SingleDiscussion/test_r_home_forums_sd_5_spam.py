import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
import pytest
import allure


def test_homeforums_id_filter_5(driver):

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

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW35'
    # android_widget_imageview35 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView")
    # android_widget_imageview35.click()
    ellipsise_single_discussion = driver.find_element(By.XPATH,
                                                      "//android.view.ViewGroup[2]/android.widget.TextView[@text = '']")
    ellipsise_single_discussion.click()

    time.sleep(5)

    # 5. Click 'Spam'
    spam = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Spam']")
    spam.click()

    time.sleep(5)

    # 6. Does 'No replies found' contain 'No replies found'?
    no_replies_found = driver.find_element(By.XPATH,
                                           "//android.widget.TextView[@text = 'No replies found']")
    step_output = no_replies_found.text
    assert step_output and ("No replies found" in step_output)

    # 7. Click 'ANDROID.WIDGET.IMAGEVIEW34'
    android_widget_imageview34 = driver.find_element(By.XPATH,
                                                     "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView")
    android_widget_imageview34.click()

    time.sleep(5)

    # 8. Click 'Unspam'
    unspam = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Unspam']")
    unspam.click()