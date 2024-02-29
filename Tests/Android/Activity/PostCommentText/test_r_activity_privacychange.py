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


def test_activity_edit_privacychange(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click ''
    # click world icon
    _ = driver.find_element(By.XPATH,
                            "//android.widget.TextView[@text = '']")
    _.click()

    time.sleep(5)

    # 3. Click 'All Members'
    all_members = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'All Members']")
    all_members.click()

    time.sleep(5)

    # 4. Click '1'
    _1 = driver.find_element(By.XPATH,
                             "//android.widget.TextView[@text = '']")
    _1.click()

    time.sleep(5)

    # 5. Click 'Public'
    public = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Public']")
    public.click()