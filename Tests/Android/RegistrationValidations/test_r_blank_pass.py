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


def test_blank_pass(driver):

    driver.reset()
    time.sleep(20)

    # 1. Click 'Don't have an account? Sign Up'
    don_t_have_an_account_question_mark_sign_up = driver.find_element(By.XPATH, "//android.view.ViewGroup[7]/android.widget.TextView")
    don_t_have_an_account_question_mark_sign_up.click()

    time.sleep(5)

    # 2. Click 'Enter email'
    # enter_email = driver.find_element(By.XPATH,
    #                                   "//android.widget.EditText[@text = 'Enter email']")
    # enter_email.click()

    # 3. Type 'emmanuel@buddyboss.com' in 'Enter email'
    enter_email = driver.find_element(By.XPATH,
                                      "//android.widget.EditText[@text = 'Enter email']")
    enter_email.send_keys("emmanuel@buddyboss.com")

    # 4. Click 'Enter confirm email'
    # enter_confirm_email = driver.find_element(By.XPATH,
    #                                           "//android.widget.EditText[@text = 'Enter confirm email']")
    # enter_confirm_email.click()

    # 5. Type 'emmanuel@buddyboss.com' in 'Enter confirm email'
    enter_confirm_email = driver.find_element(By.XPATH,
                                              "//android.widget.EditText[@text = 'Enter confirm email']")
    enter_confirm_email.send_keys("emmanuel@buddyboss.com")

    # 6. Make a Swipe gesture from ('702','1167') to ('759','307')
    driver.swipe(start_x=702, start_y=1167, end_x=759, end_y=800, duration=300)

    # 7. Click 'Enter first name1'
    enter_first_name1 = driver.find_element(By.XPATH,
                                            "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name1.click()

    # 8. Type 'emman' in 'Enter first name1'
    enter_first_name1 = driver.find_element(By.XPATH,
                                            "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name1.send_keys("emman")

    # 9. Make a Swipe gesture from ('640','1232') to ('628','658')
    driver.swipe(start_x=640, start_y=1232, end_x=628, end_y=658, duration=300)

    # 10. Click 'Enter last name'
    enter_last_name = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name.click()

    # 11. Type 'bb' in 'Enter last name'
    enter_last_name = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name.send_keys("bb")

    # 12. Make a Swipe gesture from ('601','1179') to ('595','699')
    driver.swipe(start_x=601, start_y=1179, end_x=595, end_y=699, duration=300)

    # 13. Click 'Enter nickname'
    enter_nickname = driver.find_element(By.XPATH,
                                         "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname.click()

    # 14. Type 'emmanbb' in 'Enter nickname'
    enter_nickname = driver.find_element(By.XPATH,
                                         "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname.send_keys("emmanbb")

    # 15. Click 'ANDROID.VIEW.VIEWGROUP'
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup")
    android_view_viewgroup.click()

    # 16. Click 'Create Account'
    create_account = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Create Account']")
    create_account.click()

    # 17. 'Enter a valid email' contains text '[NONE]'?
    enter_a_valid_email = (By.ID, "android:id/message")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *enter_a_valid_email)