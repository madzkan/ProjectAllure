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


def test_more_groups_single_mems_1(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(10)

    # 2. Make a Swipe gesture from ('432','1982') to ('446','1009')
    driver.swipe(start_x=432, start_y=1982,
                 end_x=446, end_y=1009, duration=300)
    time.sleep(5)

    # 3. Click 'Members1'
    members1 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Members']")
    members1.click()

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

    time.sleep(5)

    # 6. Does 'No members found' contain 'No members found'?
    no_members_found = driver.find_element(By.XPATH,
                                           "//android.widget.TextView[@text = 'No members found']")
    step_output = no_members_found.text
    assert step_output and ("No members found" in step_output)