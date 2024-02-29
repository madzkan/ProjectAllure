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


def test_more_groups_unsearchable(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(5)

    # 2. Swipe 'Up' to 'Groups - More'
    # groups_more = (
    #     By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    # driver.addons().execute(
    #     SwipeAndFindElement.verticalswipeandroid(
    #         swipeDirection="Up",
    #         bottomMarginPercent=0,
    #         topMarginPercent=0,
    #         maxSwipes=1,
    #         timeoutMilliseconds=0), *groups_more)

    # 2. Make a Swipe gesture from ('637','1342') to ('646','860')
    driver.swipe(start_x=637, start_y=1342, end_x=646, end_y=860, duration=300)

    time.sleep(3)

    # 3. Click 'Groups2'
    groups2 = driver.find_element(By.XPATH,
                                  "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    groups2.click()

    time.sleep(5)

    # 4. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    time.sleep(5)

    # 5. Type 'bbb' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("bbb")

    # 6. Does 'No groups to show' contain 'No groups to show'?
    no_groups_to_show = driver.find_element(By.XPATH,
                                            "//android.widget.TextView[@text = 'No groups to show']")
    step_output = no_groups_to_show.text
    assert step_output and ("No groups to show" in step_output)

