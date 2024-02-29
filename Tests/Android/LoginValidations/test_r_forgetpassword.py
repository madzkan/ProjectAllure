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


def test_forgotpass(driver):

    driver.reset()
    time.sleep(20)

    forgot_password_question_mark_ = driver.find_element(By.XPATH,
                                                              "//android.widget.TextView[@text = 'Forgot Password?']")
    forgot_password_question_mark_.click()

    time.sleep(5)

    email_address = driver.find_element(By.XPATH, "//android.widget.EditText[@text = 'Email Address']")
    email_address.send_keys("guest15265@buddyboss.com")

    time.sleep(5)

    android_view_viewgroup1 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Submit']")
    android_view_viewgroup1.click()