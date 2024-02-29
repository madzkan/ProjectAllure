import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from addons.swipe_and_find_element import SwipeAndFindElement
import pytest
import allure


def test_home_groups_feed(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Swipe 'Up' to 'Groups - Home'
    groups_home = (
        By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    driver.addons().execute(
        SwipeAndFindElement.verticalswipeandroid(
            swipeDirection="Up",
            bottomMarginPercent=0,
            topMarginPercent=0,
            maxSwipes=0,
            timeoutMilliseconds=0), *groups_home)

    # 2. Click 'See all7'
    see_all7 = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'See all']")
    see_all7.click()

    # 3. Click 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.click()

    # 4. Type 'bb' in 'Search'
    search = driver.find_element(By.XPATH,
                                 "//android.widget.EditText[@text = 'Search']")
    search.send_keys("bb")

    # 5. Is 'ANDROID.VIEW.VIEWGROUP13' is clickable?
    android_view_viewgroup13 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup13.is_enabled()