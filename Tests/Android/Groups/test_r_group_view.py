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

def test_groups_group_view(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    time.sleep(5)

    # 1. Click 'Groups2'
    groups2 = driver.find_element(By.XPATH,
                                  "//android.widget.TextView[1][@text = 'Groups']")
    groups2.click()

    # # 2. 'All Groups' contains text '[NONE]'?
    # # get all groups text
    # all_groups = (By.XPATH, "//android.widget.TextView[@text = 'All Groups']")
    # driver.addons().execute(
    #     VisibleElementsOperations.containstextifvisibleandroid(
    #         text="",
    #         timeout=""), *all_groups)
    #
    # # 3. 'Groups1' contains text '[NONE]'?
    # # get Groups title
    # groups1 = (
    #     By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    # driver.addons().execute(
    #     VisibleElementsOperations.containstextifvisibleandroid(
    #         text="",
    #         timeout=""), *groups1)