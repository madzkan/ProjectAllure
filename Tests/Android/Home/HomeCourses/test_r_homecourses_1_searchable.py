import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
import pytest
import allure


def test_homecourses_searchable(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'See all'
    see_all = driver.find_element(By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'See all']")
    see_all.click()

    # 2. Does '27' contain '27'?
    # _27 = driver.find_element(By.XPATH,  "//android.widget.TextView[@text = '27']")
    # step_output = _27.text
    # assert step_output and ("27" in step_output)

    time.sleep(15)

    # 3. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    # 4. Type 'bb' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("bb")
    #
    # # 5. Does '18' contain '18'?
    # _18 = driver.find_element(By.XPATH,
    #                           "//android.widget.TextView[@text = '18']")
    # step_output = _18.text
    # assert step_output and ("18" in step_output)