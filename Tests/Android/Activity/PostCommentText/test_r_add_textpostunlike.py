import time

from addons.visible_elements_operations import VisibleElementsOperations
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
def test_activity_add_text_post_unlike(driver):
    LoginTest = "Login"

    driver.reset()
    time.sleep(10)

    login = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Login']")
    step_output = login.get_attribute("text")
    assert step_output == "Login"

    LoginTest = step_output


    if f'{LoginTest}' == "Login":
        test_logintest.test_login(driver)

        # 1. Click 'Activity'
        activity = driver.find_element(By.XPATH,
                                       "//android.widget.TextView[@text = 'Activity']")
        activity.click()

        # 2. Does '1' contain '1'?
        _1 = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = '1']")
        step_output = _1.text
        assert step_output and ("1" in step_output)

        # 3. Click ''
        _ = driver.find_element(By.XPATH,
                                "//android.view.ViewGroup[3]/android.widget.TextView[@text = '']")
        _.click()

