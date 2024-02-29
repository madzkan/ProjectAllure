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


def test_more_courses_unsearchable(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    # 2. Click 'Courses5'
    courses5 = driver.find_element(By.XPATH,
                                   "//android.view.ViewGroup/android.widget.TextView[@text = 'Courses']")
    courses5.click()

    # 3. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    # 4. Type 'bbb' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("bbb")

    # 5. Does 'No Courses have been found' contain 'No Courses have been found'?
    no_courses_have_been_found = driver.find_element(By.XPATH,
                                                     "//android.widget.TextView[@text = 'No Courses have been found']")
    step_output = no_courses_have_been_found.text
    assert step_output and ("No Courses have been found" in step_output)