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


def test_homeforums_id_filter_10(driver):

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

    # 2. click single forum
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

    # 4. Swipe 'Up' to 'Manage hf ie'
    # manage_hf_ie = (By.XPATH, "//android.widget.TextView[@text = 'Manage']")
    # driver.addons().execute(
    #     SwipeAndFindElement.verticalswipeandroid(
    #         swipeDirection="Up",
    #         bottomMarginPercent=0,
    #         topMarginPercent=0,
    #         maxSwipes=0,
    #         timeoutMilliseconds=0), *manage_hf_ie)

    driver.swipe(start_x=1023, start_y=1183, end_x=945, end_y=466, duration=300)

    # 5. Click 'Manage hf ie'
    manage_hf_ie = driver.find_element(By.XPATH,
                                       "//android.widget.TextView[@text = 'Manage']")
    manage_hf_ie.click()

    time.sleep(5)

    # 6. Does 'Manage' contain 'Manage'?
    manage = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Manage']")
    step_output = manage.text
    assert step_output and ("Manage" in step_output)