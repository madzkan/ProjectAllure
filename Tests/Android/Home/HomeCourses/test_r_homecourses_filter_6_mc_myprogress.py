import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
import pytest
import allure


def test_homecourses_filter_6(driver):

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

    time.sleep(4)

    # 3. Click 'My Courses'
    my_courses = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'My Courses']")
    my_courses.click()

    time.sleep(4)

    # 4. Click 'My Progress'
    my_progress = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'My Progress']")
    my_progress.click()

    time.sleep(4)

    # 5. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    android_widget_imageview29 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    android_widget_imageview29.click()

    time.sleep(4)

    # 6. Does 'My Courses1' contain 'My Courses'?
    my_courses1 = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'My Courses']")
    step_output = my_courses1.text
    assert step_output and ("My Courses" in step_output)

    time.sleep(4)

    # 7. Does 'My Progress1' contain 'My Progress'?
    my_progress1 = driver.find_element(By.XPATH,
                                       "//android.widget.TextView[@text = 'My Progress']")
    step_output = my_progress1.text
    assert step_output and ("My Progress" in step_output)