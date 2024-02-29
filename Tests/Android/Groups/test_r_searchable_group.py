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


def test_groups_filter_2(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    time.sleep(5)

    # 1. Click 'Groups2'
    groups2 = driver.find_element(By.XPATH,
                                  "//android.widget.TextView[1][@text = 'Groups']")
    groups2.click()

    time.sleep(5)

    # 2. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    time.sleep(5)

    # 3. Type 'bb' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("bb")

    time.sleep(5)

    # 4. Does 'Foodie’s Group' contain 'Foodie’s Group'?
    foodie_s_group = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Foodie’s Group']")
    step_output = foodie_s_group.text
    assert step_output and ("Foodie’s Group" in step_output)