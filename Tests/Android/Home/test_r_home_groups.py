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


def test_home_groups(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Swipe 'Up' to 'Groups'
    # swipe to group
    groups = (
        By.XPATH, "//android.view.ViewGroup/android.widget.TextView[1][@text = 'Groups']")
    driver.addons().execute(
        SwipeAndFindElement.verticalswipeandroid(
            swipeDirection="Up",
            bottomMarginPercent=0,
            topMarginPercent=0,
            maxSwipes=0,
            timeoutMilliseconds=0), *groups)

    # 2. Click 'See all2' if it's visible
    # click see all
    see_all2 = (
        By.XPATH,
        "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'See all']")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *see_all2)

    # 3. 'Groups1' contains text '[NONE]'?
    # check if Groups visible
    groups1 = (
        By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *groups1)

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW12' if it's visible
    # click back button
    android_widget_imageview12 = (
        By.XPATH,
        "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]//android.widget.ImageView")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview12)

    # 5. Click 'ANDROID.WIDGET.IMAGEVIEW18' if it's visible
    # click on Group profile
    android_widget_imageview18 = (
        By.XPATH,
        "//android.widget.HorizontalScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView[1]")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview18)

    # 6. Click 'ANDROID.WIDGET.IMAGEVIEW19' if it's visible
    # click back button
    android_widget_imageview19 = (
        By.XPATH,
        "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview19)