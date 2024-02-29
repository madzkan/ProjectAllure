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


def test_homeforums_filter_1(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    time.sleep(5)

    # 1. Click 'See all4'
    # see_all4 = driver.find_element(By.XPATH,"//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'See all']")
    # see_all4.click()
    # see_all_forums = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Forums']/following::android.widget.TextView[@text = 'See all']")
    # see_all_forums.click()

    see_all_forums = driver.find_element(By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView")
    see_all_forums.click()

    time.sleep(10)

    # 2. Click 'Alphabetical3'
    alphabetical3 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Alphabetical']")
    alphabetical3.click()

    time.sleep(5)

    # 3. Does 'Alphabetical3' contain 'Alphabetical'?
    alphabetical3 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Alphabetical']")
    step_output = alphabetical3.text
    assert step_output and ("Alphabetical" in step_output)