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


def test_more_groups_single_feed_a_1(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    # 2. Make a Swipe gesture from ('637','1342') to ('646','860')
    driver.swipe(start_x=637, start_y=1342, end_x=646, end_y=860, duration=300)

    # 3. Click 'Groups'
    groups = driver.find_element(By.XPATH,
                                 "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    groups.click()

    # 4. Click 'ANDROID.VIEW.VIEWGROUP'
    android_view_viewgroup = driver.find_element(By.XPATH,
                                                 "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    android_view_viewgroup.click()

    # 5. Click 'Feed'
    feed = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Feed']")
    feed.click()

    # 6. Click 'ANDROID.WIDGET.IMAGEVIEW2'
    # android_widget_imageview2 = driver.find_element(By.XPATH,
    #                                                 "//android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview2.click()
    click_pencil = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    click_pencil.click()

    # 7. Click 'Write here or use @ to mention someone.'
    write_here_or_use_to_mention_someone_ = driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Write here or use @ to mention someone.']")
    write_here_or_use_to_mention_someone_.click()

    # 8. Type 'bbb' in 'Write here or use @ to mention someone.'
    #
    driver.press_keycode(30)
    driver.press_keycode(30)
    driver.press_keycode(30)

    # 9. Click 'Post'
    post = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Post']")
    post.click()

    # 10. Does 'bbb' contain 'bbb'?
    bbb = driver.find_element(By.XPATH,
                              "//android.widget.TextView[@text = 'bbb']")
    step_output = bbb.text
    assert step_output and ("bbb" in step_output)