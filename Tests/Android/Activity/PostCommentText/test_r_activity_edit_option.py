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


def test_activity_edit_option(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # 2. Click '4'
    # click ellip option
    # _4 = driver.find_element(By.XPATH, "//android.view.ViewGroup[5]/android.widget.TextView[@text = '']")
    # _4.click()

    _4 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    _4.click()

    time.sleep(5)

    # 3. Click 'Edit'
    edit = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Edit']")
    edit.click()

    time.sleep(5)

    # 4. Does 'Edit Post' contain 'Edit Post'?
    edit_post = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'Edit Post']")
    step_output = edit_post.text
    assert step_output and ("Edit Post" in step_output)

    # 5. Click 'Cancel'
    cancel = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Cancel']")
    cancel.click()
