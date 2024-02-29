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


    #Check if home tite is existing
    home = (
        By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Home']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *home)

    #Check if courses widget title exist
    courses = (
        By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Courses']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *courses)

    #Click 'See all' Course if it's visible
    see_all = (
        By.XPATH,
        "//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'See all']")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *see_all)
