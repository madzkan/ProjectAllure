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


def test_wrongpassword(driver):

    driver.reset()
    time.sleep(20)

    login_username_input = driver.find_element(By.XPATH,
                                                    "//android.widget.EditText[@content-desc = 'login_username_input']")
    login_username_input.send_keys("john")

    login_password_input = driver.find_element(By.XPATH,
                                                    "//android.widget.EditText[@content-desc = 'login_password_input']")
    login_password_input.send_keys("123456!xxx")

    login_test = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Login']")
    login_test.click()