import time

from selenium.webdriver.common.by import By

from appium import webdriver

import pytest
import allure


def test_activity_view(setUp):


    driver.reset()
    time.sleep(10)

    login = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Login']")
    step_output = login.get_attribute("text")
    assert step_output == "Login"

    LoginTest = step_output


    if f'{LoginTest}' == "Login":
        test_userlogin.test_login(driver)

        # com_android_permissioncontroller_colon_id_slash_g_ = driver.find_element(By.ID,
        #                                                                          "com.android.permissioncontroller:id/grant_singleton")
        # com_android_permissioncontroller_colon_id_slash_g_.click()
        #
        # # 4. Click 'com.android.permissioncontroller:id/g...'
        # com_android_permissioncontroller_colon_id_slash_g_ = driver.find_element(By.ID,
        #                                                                          "com.android.permissioncontroller:id/grant_singleton")
        # com_android_permissioncontroller_colon_id_slash_g_.click()

        # 1. Click 'More'
        more = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'More']")
        more.click()

        # 2. 'More1' contains text '[NONE]'?
        more1 = (
            By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'More']")
        driver.addons().execute(
            VisibleElementsOperations.containstextifvisibleandroid(
                text="",
                timeout=""), *more1)