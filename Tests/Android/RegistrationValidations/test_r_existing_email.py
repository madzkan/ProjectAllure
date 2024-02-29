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


def test_existing_email(driver):

    driver.reset()
    time.sleep(20)

    don_t_have_an_account_question_mark_sign_up = driver.find_element(By.XPATH,
                                                                      "//android.view.ViewGroup[7]/android.widget.TextView")
    don_t_have_an_account_question_mark_sign_up.click()

    time.sleep(5)

    # 1. Click 'Enter email'
    enter_email = driver.find_element(By.XPATH,
                                      "//android.widget.EditText[@text = 'Enter email']")
    enter_email.click()

    # 2. Type 'guest15265@buddyboss.com' in 'Enter email'
    enter_email = driver.find_element(By.XPATH,
                                      "//android.widget.EditText[@text = 'Enter email']")
    enter_email.send_keys("guest15265@buddyboss.com")

    # 3. Click 'Enter confirm email'
    enter_confirm_email = driver.find_element(By.XPATH,
                                              "//android.widget.EditText[@text = 'Enter confirm email']")
    enter_confirm_email.click()

    # 4. Type 'guest15265@buddyboss.com' in 'Enter confirm email'
    enter_confirm_email = driver.find_element(By.XPATH,
                                              "//android.widget.EditText[@text = 'Enter confirm email']")
    enter_confirm_email.send_keys("guest15265@buddyboss.com")

    # 5. Click 'Enter password1'
    enter_password1 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter password']")
    enter_password1.click()

    # 6. Type 'kenawuvi71' in 'Enter password1'
    enter_password1 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter password']")
    enter_password1.send_keys("kenawuvi71")

    # 7. Make a Swipe gesture from ('810','1193') to ('778','862')
    driver.swipe(start_x=810, start_y=1193, end_x=778, end_y=862, duration=300)

    # 8. Click 'Enter confirm password'
    enter_confirm_password = driver.find_element(By.XPATH,
                                                 "//android.widget.EditText[@text = 'Enter confirm password']")
    enter_confirm_password.click()

    # 9. Type 'kenawuvi71' in 'Enter confirm password'
    enter_confirm_password = driver.find_element(By.XPATH,
                                                 "//android.widget.EditText[@text = 'Enter confirm password']")
    enter_confirm_password.send_keys("kenawuvi71")

    # 10. Make a Swipe gesture from ('810','1193') to ('778','862')
    driver.swipe(start_x=810, start_y=1193, end_x=778, end_y=862, duration=300)

    # 11. Click 'Enter first name1'
    enter_first_name1 = driver.find_element(By.XPATH,
                                            "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name1.click()

    # 12. Type 'john' in 'Enter first name1'
    enter_first_name1 = driver.find_element(By.XPATH,
                                            "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name1.send_keys("john")

    # 13. Make a Swipe gesture from ('810','1193') to ('778','862')
    driver.swipe(start_x=810, start_y=1193, end_x=778, end_y=862, duration=300)

    # 14. Click 'Enter last name'
    enter_last_name = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name.click()

    # 15. Type 'smith' in 'Enter last name'
    enter_last_name = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name.send_keys("smith")

    # 16. Make a Swipe gesture from ('810','1193') to ('778','862')
    driver.swipe(start_x=810, start_y=1193, end_x=778, end_y=862, duration=300)

    # 17. Click 'Enter nickname2'
    enter_nickname2 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname2.click()

    # 18. Type 'john' in 'Enter nickname2'
    enter_nickname2 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname2.send_keys("john")

    # 19. Make a Swipe gesture from ('810','1193') to ('778','862')
    driver.swipe(start_x=810, start_y=1193, end_x=778, end_y=862, duration=300)

    # 20. Click 'ANDROID.VIEW.VIEWGROUP'
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup")
    android_view_viewgroup.click()

    # 21. Click 'ANDROID.VIEW.VIEWGROUP1'
    android_view_viewgroup1 = driver.find_element(By.XPATH,
                                                  "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup")
    android_view_viewgroup1.click()

    # 22. 'Enter a valid email' contains text '[NONE]'?
    enter_a_valid_email = (By.ID, "android:id/message")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *enter_a_valid_email)