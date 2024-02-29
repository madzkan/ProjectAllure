import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
import pytest
import allure


def test_homecourses_filter_3(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Click 'See all'
    see_all = driver.find_element(By.XPATH,
                                  "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'See all']")
    see_all.click()

    time.sleep(10)

    # 2. Click 'ANDROID.WIDGET.IMAGEVIEW30'
    # android_widget_imageview30 = driver.find_element(By.XPATH,
    #                                                  "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    # android_widget_imageview30.click()
    android_widget_imageview30 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    android_widget_imageview30.click()

    time.sleep(5)

    # 3. Click 'All Courses'
    all_courses = driver.find_element(By.XPATH,
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'All Courses']")
    all_courses.click()

    time.sleep(5)

    # 4. Click 'Alphabetical'
    alphabetical = driver.find_element(By.XPATH,
                                       "//android.view.ViewGroup[1]/android.widget.TextView[@text = 'Alphabetical']")
    alphabetical.click()

    time.sleep(5)

    # 5. Click 'Alphabetical1'
    alphabetical1 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Alphabetical']")
    alphabetical1.click()

    time.sleep(5)

    # 6. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    android_widget_imageview29 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    android_widget_imageview29.click()

    time.sleep(5)

    # 7. Does 'Alphabetical2' contain 'Alphabetical'?
    alphabetical2 = driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'Alphabetical']")
    step_output = alphabetical2.text
    assert step_output and ("Alphabetical" in step_output)