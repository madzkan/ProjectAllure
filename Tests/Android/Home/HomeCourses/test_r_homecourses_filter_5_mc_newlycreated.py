import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
import pytest
import allure


def test_homecourses_filter_5(driver):

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

    time.sleep(3)

    # 3. Click 'My Courses'
    my_courses = driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'My Courses']")
    my_courses.click()

    time.sleep(4)

    # 4. Click 'Newly Created2'
    newly_created2 = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Newly Created']")
    newly_created2.click()

    time.sleep(4)

    # 5. Click 'ANDROID.VIEW.VIEWGROUP11'
    # android_view_viewgroup11 = driver.find_element(By.XPATH,
    #                                                "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
    # android_view_viewgroup11.click()

    android_widget_imageview29 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    android_widget_imageview29.click()

    time.sleep(4)

    # 6. Does 'My Courses1' contain 'My Courses'?
    my_courses1 = driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'My Courses']")
    step_output = my_courses1.text
    assert step_output and ("My Courses" in step_output)

    time.sleep(4)

    # 7. Does 'Newly Created3' contain 'Newly Created'?
    newly_created3 = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Newly Created']")
    step_output = newly_created3.text
    assert step_output and ("Newly Created" in step_output)
