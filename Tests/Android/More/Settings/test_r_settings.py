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


def test_settings(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    # 2. Click 'Settings2'
    settings2 = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'Settings']")
    settings2.click()

    # 3. Does 'Settings1' contain 'Settings'?
    settings1 = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'Settings']")
    step_output = settings1.text
    assert step_output and ("Settings" in step_output)

    # 4. Is 'Login Information' is clickable?
    login_information = driver.find_element(By.XPATH,
                                            "//android.widget.TextView[@text = 'Login Information']")
    assert login_information.is_enabled()

    # 5. Is 'Notification Preferences' is clickable?
    notification_preferences = driver.find_element(By.XPATH,
                                                   "//android.widget.TextView[@text = 'Notification Preferences']")
    assert notification_preferences.is_enabled()

    # 6. Is 'Privacy Settings' is clickable?
    privacy_settings = driver.find_element(By.XPATH,
                                           "//android.widget.TextView[@text = 'Privacy Settings']")
    assert privacy_settings.is_enabled()

    # 7. Is 'Group Invites' is clickable?
    group_invites = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Group Invites']")
    assert group_invites.is_enabled()

    # 8. Is 'Export Data' is clickable?
    export_data = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'Export Data']")
    assert export_data.is_enabled()

    # 9. Is 'About' is clickable?
    about = driver.find_element(By.XPATH,
                                "//android.widget.TextView[@text = 'About']")
    assert about.is_enabled()