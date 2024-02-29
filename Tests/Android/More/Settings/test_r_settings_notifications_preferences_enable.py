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


def test_settings_notif_pref_enable(driver):

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

    # 3. Click 'Notification Preferences'
    notification_preferences = driver.find_element(By.XPATH,
                                                   "//android.widget.TextView[@text = 'Notification Preferences']")
    notification_preferences.click()

    # 4. Does 'Notification Preferences1' contain 'Notification Preferences'?
    notification_preferences1 = driver.find_element(By.XPATH,
                                                    "//android.widget.TextView[@text = 'Notification Preferences']")
    step_output = notification_preferences1.text
    assert step_output and ("Notification Preferences" in step_output)

    # 5. Does 'Email, App' contain 'Email, App'?
    email_app = driver.find_element(By.XPATH,
                                    "//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'Email, App']")
    step_output = email_app.text
    assert step_output and ("Email, App" in step_output)

    # 6. Click 'Email, App'
    email_app = driver.find_element(By.XPATH,
                                    "//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'Email, App']")
    email_app.click()

    # 7. Does 'Preferences' contain 'Preferences'?
    preferences = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'Preferences']")
    step_output = preferences.text
    assert step_output and ("Preferences" in step_output)

    # 8. Click 'ANDROID.WIDGET.IMAGEVIEW'
    android_widget_imageview = driver.find_element(By.XPATH,
                                                   "//android.view.ViewGroup[2]/android.widget.ImageView")
    android_widget_imageview.click()
