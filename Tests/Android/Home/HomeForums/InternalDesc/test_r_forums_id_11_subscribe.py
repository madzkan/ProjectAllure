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


def test_homeforums_id_filter_11(driver):

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

    # 2. Click 'Architecture'
    architecture = driver.find_element(By.XPATH,
                                       "//android.widget.TextView[@text = 'Architecture']")
    architecture.click()

    time.sleep(5)

    # 3. Click 'Every man's work, whether it be liter...1'
    every_man_s_work_whether_it_be_liter_1 = driver.find_element(By.XPATH,
                                                                 "//android.widget.TextView[@text = concat('Every man', \"'\", 's work, whether it be literature, or music or pictures or architecture or anything else, is always a portrait of himself.')]")
    every_man_s_work_whether_it_be_liter_1.click()

    time.sleep(5)

    # 4. Does 'Subscribe' contain 'Subscribe'?
    subscribe = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Subscribe']")
    step_output = subscribe.text
    assert step_output and ("Subscribe" in step_output)

    # 5. Click 'Subscribe'
    subscribe = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'Subscribe']")
    subscribe.click()
