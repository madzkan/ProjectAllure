import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
import pytest
import allure


def test_homecourses_unsearchable(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'See all'
    see_all = driver.find_element(By.XPATH,
                                  "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'See all']")
    see_all.click()

    time.sleep(10)

    # 2. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    # 3. Type 'aaa' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("aaa")

    # 4. Does 'No Courses have been found' contain 'No Courses have been found'?
    # no_courses_have_been_found = driver.find_element(By.XPATH,
    #                                                  "//android.widget.TextView[@text = 'No Courses have been found']")
    # step_output = no_courses_have_been_found.text
    # assert step_output and ("No Courses have been found" in step_output)