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


def test_activity_pp_postall(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'Activity'
    activity = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Activity']")
    activity.click()

    time.sleep(5)

    # # 2. 'News Feed' contains text '[NONE]'?
    # news_feed = (By.XPATH, "//android.widget.TextView[@text = 'News Feed']")
    # driver.addons().execute(
    #     VisibleElementsOperations.containstextifvisibleandroid(
    #         text="",
    #         timeout=""), *news_feed)
    #
    # # 3. Is 'ANDROID.WIDGET.IMAGEVIEW20' clickable?
    # android_widget_imageview20 = (
    #     By.XPATH,
    #     "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # driver.addons().execute(
    #     VisibleElementsOperations.isclickableandroid(
    #         timeout=""), *android_widget_imageview20)

    # 1. Click 'ANDROID.WIDGET.IMAGEVIEW10'
    # android_widget_imageview10 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview10.click()
    pen_btn = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    pen_btn.click()

    time.sleep(5)

    # 2. Click 'Public'
    public = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Public']")
    public.click()

    time.sleep(5)

    # 3. Click 'All Members'
    all_members = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'All Members']")
    all_members.click()

    time.sleep(5)

    # 4. Click 'Write here or use @ to mention someone.'
    write_here_or_use_to_mention_someone_ = driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Write here or use @ to mention someone.']")
    write_here_or_use_to_mention_someone_.click()

    time.sleep(5)

    # 5. Click 'Write here or use @ to mention someone.'
    write_here_or_use_to_mention_someone_ = driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Write here or use @ to mention someone.']")
    write_here_or_use_to_mention_someone_.click()

    time.sleep(5)

    # 6. Type 'test all mem' in 'Write here or use @ to mention someone.'
    write_here_or_use_to_mention_someone_ = driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Write here or use @ to mention someone.']")
    write_here_or_use_to_mention_someone_.send_keys("test all mem")

    # 7. Click 'Post'
    post = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Post']")
    post.click()