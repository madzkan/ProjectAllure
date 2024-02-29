import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
import pytest
import allure


def test_homecourses_filter_1(driver):

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

    time.sleep(10)

    # 3. Click 'Newly Created2'
    newly_created2 = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'Newly Created']")
    newly_created2.click()

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    android_widget_imageview29 = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    android_widget_imageview29.click()

    time.sleep(3)

    # 5. Does 'Newly Created3' contain 'Newly Created'?
    # newly_created3 = driver.find_element(By.XPATH,
    #                                      "//android.widget.TextView[@text = 'Newly Created']")
    # step_output = newly_created3.text
    # assert step_output and ("Newly Created" in step_output)