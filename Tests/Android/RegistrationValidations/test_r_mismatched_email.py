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


def test_mismatched_email(driver):

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

    # 2. Type 'emmanuel@buddyboss.com' in 'Enter email'
    enter_email = driver.find_element(By.XPATH,
                                      "//android.widget.EditText[@text = 'Enter email']")
    enter_email.send_keys("emmanuel@buddyboss.com")

    # 3. Click 'Enter confirm email'
    enter_confirm_email = driver.find_element(By.XPATH,
                                              "//android.widget.EditText[@text = 'Enter confirm email']")
    enter_confirm_email.click()

    # 4. Type 'emmanuel1@buddyboss.com' in 'Enter confirm email'
    enter_confirm_email = driver.find_element(By.XPATH,
                                              "//android.widget.EditText[@text = 'Enter confirm email']")
    enter_confirm_email.send_keys("emmanuel1@buddyboss.com")

    # 5. Click 'Enter password1'
    enter_password1 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter password']")
    enter_password1.click()

    # 6. Type '123456!' in 'Enter password1'
    enter_password1 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter password']")
    enter_password1.send_keys("123456!")

    # 7. Make a Swipe gesture from ('489','1357') to ('630','936')
    driver.swipe(start_x=489, start_y=1357, end_x=630, end_y=936, duration=300)

    # 8. Click 'Enter confirm password'
    enter_confirm_password = driver.find_element(By.XPATH,
                                                 "//android.widget.EditText[@text = 'Enter confirm password']")
    enter_confirm_password.click()

    # 9. Type '123456!' in 'Enter confirm password'
    enter_confirm_password = driver.find_element(By.XPATH,
                                                 "//android.widget.EditText[@text = 'Enter confirm password']")
    enter_confirm_password.send_keys("123456!")

    # 10. Make a Swipe gesture from ('489','1357') to ('630','936')
    driver.swipe(start_x=489, start_y=1357, end_x=630, end_y=936, duration=300)

    # 11. Click 'Enter first name1'
    enter_first_name1 = driver.find_element(By.XPATH,
                                            "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name1.click()

    # 12. Type 'emman' in 'Enter first name1'
    enter_first_name1 = driver.find_element(By.XPATH,
                                            "//android.widget.EditText[@text = 'Enter first name']")
    enter_first_name1.send_keys("emman")

    # 13. Make a Swipe gesture from ('489','1357') to ('630','936')
    driver.swipe(start_x=489, start_y=1357, end_x=630, end_y=936, duration=300)

    # 14. Click 'Enter last name2'
    enter_last_name2 = driver.find_element(By.XPATH,
                                           "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name2.click()

    # 15. Type 'bb' in 'Enter last name2'
    enter_last_name2 = driver.find_element(By.XPATH,
                                           "//android.widget.EditText[@text = 'Enter last name']")
    enter_last_name2.send_keys("bb")

    # 16. Click 'Enter nickname2'
    enter_nickname2 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname2.click()

    # 17. Type 'emmanbb' in 'Enter nickname2'
    enter_nickname2 = driver.find_element(By.XPATH,
                                          "//android.widget.EditText[@text = 'Enter nickname']")
    enter_nickname2.send_keys("emmanbb")

    # 18. Make a Swipe gesture from ('489','1357') to ('630','936')
    driver.swipe(start_x=489, start_y=1357, end_x=630, end_y=936, duration=300)

    # 19. Click 'ANDROID.VIEW.VIEWGROUP7'
    android_view_viewgroup7 = driver.find_element(By.XPATH,
                                                  "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup")
    android_view_viewgroup7.click()

    # 20. Make a Swipe gesture from ('489','1357') to ('630','936')
    driver.swipe(start_x=489, start_y=1357, end_x=630, end_y=936, duration=300)

    # 21. Click 'Create Account'
    create_account = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Create Account']")
    create_account.click()
