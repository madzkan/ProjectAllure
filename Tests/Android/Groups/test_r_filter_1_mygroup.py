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


def test_groups_filter_1(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    time.sleep(5)

    # 1. Click 'Groups2'
    groups2 = driver.find_element(By.XPATH,
                                  "//android.widget.TextView[1][@text = 'Groups']")
    groups2.click()

    time.sleep(10)

    # 2. Click 'ANDROID.WIDGET.IMAGEVIEW28'
    # android_widget_imageview28 = driver.find_element(By.XPATH,  "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview28.click()
    filter_click = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    filter_click.click()

    time.sleep(10)

    # 3. Click 'My Groups'
    my_groups = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'My Groups']")
    my_groups.click()

    time.sleep(5)

    # 4. Click 'ANDROID.VIEW.VIEWGROUP11'
    # android_view_viewgroup11 = driver.find_element(By.XPATH,
    #                                                "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
    # android_view_viewgroup11.click()
    close_btn1 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    close_btn1.click()


    time.sleep(5)

    # 5. Does 'My Groups1' contain 'My Groups'?
    my_groups1 = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'My Groups']")
    step_output = my_groups1.text
    assert step_output and ("My Groups" in step_output)