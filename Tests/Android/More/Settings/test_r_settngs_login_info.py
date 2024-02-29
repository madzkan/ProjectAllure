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


def test_settings_login_info(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    # 2. Click 'Settings'
    settings = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Settings']")
    settings.click()

    # 3. Click 'Login Information'
    login_information = driver.find_element(By.XPATH,
                                            "//android.widget.TextView[@text = 'Login Information']")
    login_information.click()

    # 4. Does 'Login Information1' contain 'Login Information'?
    login_information1 = driver.find_element(By.XPATH,
                                             "//android.widget.TextView[@text = 'Login Information']")
    step_output = login_information1.text
    assert step_output and ("Login Information" in step_output)
