import time

from selenium.webdriver.common.by import By


from appium import webdriver

import pytest
import allure


def test_main(driver):
    """login testing for Android."""

    driver.reset()

    time.sleep(20)