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
    blog = driver.find_element(By.XPATH,
                               "//android.widget.TextView[@text = 'Blog']")
    blog.click()

    time.sleep(10)

    # 3. Click 'All Categories'
    all_categories = driver.find_element(By.XPATH,
                                         "//android.widget.TextView[@text = 'All Categories']")
    all_categories.click()

    time.sleep(10)

    # 4. Click 'Business'
    business = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Business']")
    business.click()

    # 5. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    closebtn = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = '']")
    closebtn.click()

    # 6. Click 'Any Year'
    any_year = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = 'Any Year']")
    any_year.click()

    # 7. Click '2020'
    _2020 = driver.find_element(By.XPATH,
                                "//android.widget.TextView[@text = '2020']")
    _2020.click()

    # 8. Click 'ANDROID.WIDGET.IMAGEVIEW29'
    # android_widget_imageview29 = driver.find_element(By.XPATH,
    #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//android.widget.ImageView")
    # android_widget_imageview29.click()
    closebtn = driver.find_element(By.XPATH,
                                   "//android.widget.TextView[@text = '']")
    closebtn.click()

    # 9. Is 'ANDROID.VIEW.VIEWGROUP13' is clickable?
    android_view_viewgroup13 = driver.find_element(By.XPATH,
                                                   "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup13.is_enabled()

    # 10. Does '20201' contain '2020'?
    _20201 = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = '2020']")
    step_output = _20201.text
    assert step_output and ("2020" in step_output)