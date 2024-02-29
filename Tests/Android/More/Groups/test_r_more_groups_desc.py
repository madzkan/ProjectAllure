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

    time.sleep(5)


    # 2. Make a Swipe gesture from ('637','1342') to ('646','860')
    driver.swipe(start_x=637, start_y=1342, end_x=646, end_y=860, duration=300)

    time.sleep(3)

    # 3. Click 'Groups1'
    groups1 = driver.find_element(By.XPATH,
                                  "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    groups1.click()

    time.sleep(5)

    # 4. Click 'Organizer'
    organizer = driver.find_element(By.XPATH,
                                    "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'Organizer']")
    organizer.click()

    time.sleep(5)

    # 5. Is 'Every man’s work, whether it be liter...' present?
    every_man_s_work_whether_it_be_liter_ = driver.find_element(By.XPATH,
                                                                "//android.widget.TextView[@text = 'Every man’s work, whether it be literature, or music or pictures or architecture or anything else, is always a portrait of himself.']")