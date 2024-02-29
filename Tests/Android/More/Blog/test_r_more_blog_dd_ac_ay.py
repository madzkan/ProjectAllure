import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.actions import Actions
from addons.visible_elements_operations import VisibleElementsOperations
import pytest
import allure


def test_home_courses(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)


    # 1. Click 'More'
    more = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'More']")
    more.click()

    time.sleep(10)

    # 2. Click 'Blog'
    blog = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Blog']")
    blog.click()

    time.sleep(15)

    # 3. Click 'All Categories'
    all_categories = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'All Categories']")
    all_categories.click()

    # 4. Click 'All Categories1'
    all_categories1 = driver.find_element(By.XPATH,
                                          "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'All Categories']")
    all_categories1.click()

    # 5. Click 'All Categories2'
    all_categories2 = driver.find_element(By.XPATH,
                                          "//android.widget.TextView[@text = 'All Categories']")
    all_categories2.click()

    # 6. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    closebtn = driver.find_element(By.XPATH,
                                  "//android.widget.TextView[@text = '']")
    closebtn.click()

    # 7. Is 'ANDROID.VIEW.VIEWGROUP13' present?
    # android_view_viewgroup13 = driver.find_element(By.XPATH,
    #                                                "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    #
    # # 8. Is 'ANDROID.VIEW.VIEWGROUP13' is clickable?
    # android_view_viewgroup13 = driver.find_element(By.XPATH,
    #                                                "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    # assert android_view_viewgroup13.is_enabled()