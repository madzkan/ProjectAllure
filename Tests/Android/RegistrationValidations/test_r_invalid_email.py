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


def test_invalid_email(driver):

    driver.reset()
    time.sleep(20)
    don_t_have_an_account_question_mark_sign_up = driver.find_element(By.XPATH,
                                                                      "//android.view.ViewGroup[7]/android.widget.TextView")
    don_t_have_an_account_question_mark_sign_up.click()

    time.sleep(5)

    # 2. Click 'Enter email'
    enter_email = driver.find_element(By.XPATH,
                                      "//android.widget.EditText[@text = 'Enter email']")
    enter_email.click()

    # 3. Type 'emmanuel@buddyboss.com' in 'steve@demos.buddyboss.com'
    steve_demos_buddyboss_com = driver.find_element(By.XPATH,
                                                    "//android.widget.EditText[@text = 'Enter email']")
    steve_demos_buddyboss_com.send_keys("emmanuel")

    # 1. Click 'Enter password'
    enter_password = driver.find_element(By.XPATH,
                                         "//android.widget.EditText[@text = 'Enter password']")
    enter_password.click()

    # 2. Type '123456!' in 'Enter password'
    enter_password = driver.find_element(By.XPATH,
                                         "//android.widget.EditText[@text = 'Enter password']")
    enter_password.send_keys("123456!")

    driver.swipe(start_x=702, start_y=1167, end_x=759, end_y=800, duration=300)

    # 3. Click 'Enter first name'
    enter_first_name = driver.find_element(By.XPATH,
                                           "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name.click()

    # 4. Type 'admin2' in 'Enter first name'
    enter_first_name = driver.find_element(By.XPATH,
                                           "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name.send_keys("admin2")

    # 5. Make a Swipe gesture from ('878','1274') to ('872','492')
    driver.swipe(start_x=878, start_y=1274, end_x=872, end_y=492, duration=300)

    # 6. Click 'Enter last name1'
    enter_last_name1 = driver.find_element(By.XPATH,
                                           "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name1.click()

    # 7. Type 'admin2' in 'Enter last name1'
    enter_last_name1 = driver.find_element(By.XPATH,
                                           "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name1.send_keys("admin2")

    # 8. Click 'Enter nickname1'
    enter_nickname1 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname1.click()

    # 9. Type 'admin2' in 'Enter nickname1'
    enter_nickname1 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname1.send_keys("admin2")

    # 10. Click 'ANDROID.VIEW.VIEWGROUP'
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup")
    android_view_viewgroup.click()

    # 11. Make a Swipe gesture from ('785','1142') to ('836','672')
    driver.swipe(start_x=785, start_y=1142, end_x=836, end_y=672, duration=300)

    # 12. Click 'Create Account'
    create_account = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Create Account']")
    create_account.click()

    # 13. 'Enter a valid email' contains text '[NONE]'?
    enter_a_valid_email = (By.ID, "android:id/message")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *enter_a_valid_email)