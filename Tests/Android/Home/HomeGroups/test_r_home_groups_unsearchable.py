import time

from addons.visible_elements_operations import VisibleElementsOperations
from addons.swipe_and_find_element import SwipeAndFindElement
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.actions import Actions
from subtests import test_logintest
from vardata.varstore import udid, appPackage, appActivity, dev_token
import pytest


@pytest.fixture()
def driver():
    capabilities = {
        "platformName": "Android",
        "udid": f"{udid}",
        "appPackage": f"{appPackage}",
        "autoAcceptAlerts": True,
        "autoGrantPermissions": True,
        "appActivity": f"{appActivity}",
    }
    driver = webdriver.Remote(token=f"{dev_token}",
                              project_name="Android Automations",
                              job_name="HomePage",
                              desired_capabilities=capabilities)
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=2000,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()

@report_assertion_errors
def test_groups_filter_ag_al_ag(driver):
    LoginTest = "Login"

    driver.reset()
    time.sleep(10)

    login = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Login']")
    step_output = login.get_attribute("text")
    assert step_output == "Login"

    LoginTest = step_output


    if f'{LoginTest}' == "Login":
        test_logintest.test_login(driver)

        # 1. Swipe 'Up' to 'Groups - Home'
        groups_home = (
            By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
        driver.addons().execute(
            SwipeAndFindElement.verticalswipeandroid(
                swipeDirection="Up",
                bottomMarginPercent=0,
                topMarginPercent=0,
                maxSwipes=0,
                timeoutMilliseconds=0), *groups_home)

        # 2. Click 'See all4'
        see_all4 = driver.find_element(By.XPATH,
                                       "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup//android.widget.TextView[@text = 'See all']")
        see_all4.click()

        # 3. Click 'Search'
        search = driver.find_element(By.XPATH,
                                     "//android.widget.EditText[@text = 'Search']")
        search.click()

        # 4. Type 'sss' in 'Search'
        search = driver.find_element(By.XPATH,
                                     "//android.widget.EditText[@text = 'Search']")
        search.send_keys("sss")

        # 5. Does 'No groups to show' contain 'No groups to show'?
        no_groups_to_show = driver.find_element(By.XPATH,
                                                "//android.widget.TextView[@text = 'No groups to show']")
        step_output = no_groups_to_show.text
        assert step_output and ("No groups to show" in step_output)
