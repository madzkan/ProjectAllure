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


def test_home_forums(driver):

    # driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. 'Forums' contains text '[NONE]'?
    forums = (By.XPATH, "//android.widget.TextView[@text = 'Forums']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *forums)

    # 2. Click 'See all1' if it's visible
    see_all1 = (
        By.XPATH,
        "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[@text = 'See all']")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *see_all1)

    # 3. 'Forums1' contains text '[NONE]'?
    forums1 = (By.XPATH, "//android.widget.TextView[@text = 'Forums']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *forums1)

    # 4. Click 'ANDROID.WIDGET.IMAGEVIEW12' if it's visible
    # back button
    android_widget_imageview12 = (
        By.XPATH,
        "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]//android.widget.ImageView")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview12)

    # 5. Click 'ANDROID.WIDGET.IMAGEVIEW13' if it's visible
    # forum image
    android_widget_imageview13 = (
        By.XPATH,
        "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview13)

    # 6. 'Discussions' contains text '[NONE]'?
    # check if Discussions is existing
    discussions = (
        By.XPATH, "//android.widget.TextView[@text = 'Discussions']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *discussions)

    # 7. Click 'ANDROID.WIDGET.IMAGEVIEW14' if it's visible
    # back button
    android_widget_imageview14 = (
        By.XPATH,
        "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview14)

    # 8. Click 'Mail Check' if it's visible
    # click Forum Title
    mail_check = (By.XPATH, "//android.widget.TextView[@text = 'Mail Check']")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *mail_check)

    # 9. 'Discussions' contains text '[NONE]'?
    discussions = (
        By.XPATH, "//android.widget.TextView[@text = 'Discussions']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *discussions)

    # 10. Click 'ANDROID.WIDGET.IMAGEVIEW14' if it's visible
    # back button
    android_widget_imageview14 = (
        By.XPATH,
        "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview14)

    # 11. Click '2 Discussions' if it's visible
    _2_discussions = (
        By.XPATH, "//android.widget.TextView[@text = '2 Discussions']")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *_2_discussions)

    # 12. 'Discussions' contains text '[NONE]'?
    discussions = (
        By.XPATH, "//android.widget.TextView[@text = 'Discussions']")
    driver.addons().execute(
        VisibleElementsOperations.containstextifvisibleandroid(
            text="",
            timeout=""), *discussions)

    # 13. Click 'ANDROID.WIDGET.IMAGEVIEW14' if it's visible
    android_widget_imageview14 = (
        By.XPATH,
        "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
    driver.addons().execute(
        VisibleElementsOperations.clickifvisibleandroid(
            timeout=""), *android_widget_imageview14)