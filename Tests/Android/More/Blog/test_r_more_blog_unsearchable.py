import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.actions import Actions
from addons.visible_elements_operations import VisibleElementsOperations
import pytest
import allure


def test_home_courses(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(10)

    # 2. Click 'Blog'
    blog = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Blog']")
    blog.click()

    time.sleep(10)

    # 3. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    time.sleep(10)

    # 4. Type 'sss' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("sss")

    # 5. Does 'No posts found' contain 'No posts found'?
    no_posts_found = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'No posts found']")
    step_output = no_posts_found.text
    assert step_output and ("No posts found" in step_output)


