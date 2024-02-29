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
def test_groups_filter_ag_ra_t(driver):
    LoginTest = "Login"

    driver.reset()

    login = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Login']")
    step_output = login.get_attribute("text")
    assert step_output == "Login"

    LoginTest = step_output


    if f'{LoginTest}' == "Login":
        test_logintest.test_login(driver)

        time.sleep(10)

        # 1. Swipe 'Up' to 'Members - Home'
        members_home = (By.XPATH, "//android.widget.TextView[@text = 'Members']")
        driver.addons().execute(
            SwipeAndFindElement.verticalswipeandroid(
                swipeDirection="Up",
                bottomMarginPercent=0,
                topMarginPercent=0,
                maxSwipes=3,
                timeoutMilliseconds=0), *members_home)

        time.sleep(7)

        # 2. Click 'See all - im1'
        see_all4 = driver.find_element(By.XPATH,
                                       "//android.widget.TextView[@text = 'Members']/following::android.widget.TextView[@text = 'See all']")
        see_all4.click()

        time.sleep(7)

        # 3. Click 'All Members1'
        all_members1 = driver.find_element(By.XPATH,
                                           "//android.widget.TextView[@text = 'All Members']")
        all_members1.click()

        # 4. Click 'Connections - im'
        connections_im = driver.find_element(By.XPATH,
                                             "//android.widget.TextView[@text = 'Connections']")
        connections_im.click()

        # 5. Click 'ANDROID.WIDGET.IMAGEVIEW41'
        android_widget_imageview41 = driver.find_element(By.XPATH,
                                                         "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
        android_widget_imageview41.click()

        # 6. Click 'Recently Active3'
        recently_active3 = driver.find_element(By.XPATH,
                                               "//android.widget.TextView[@text = 'Recently Active']")
        recently_active3.click()

        # 7. Click 'Newest Members1'
        newest_members1 = driver.find_element(By.XPATH,
                                              "//android.widget.TextView[@text = 'Newest Members']")
        newest_members1.click()

        # 8. Click 'ANDROID.WIDGET.IMAGEVIEW41'
        # android_widget_imageview41 = driver.find_element(By.XPATH,
        #                                                  "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
        # android_widget_imageview41.click()
        close_btn = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
        close_btn.click()

        # 9. Is 'ANDROID.VIEW.VIEWGROUP18' is clickable?
        android_view_viewgroup18 = driver.find_element(By.XPATH,
                                                       "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
        assert android_view_viewgroup18.is_enabled()