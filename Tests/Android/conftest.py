import pytest


from appium import webdriver
from src.testproject.sdk import drivers, addons


def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

@pytest.fixture(scope="session")
def driver():
    capabilities = {
        "platformName": "Android",
        # "udid": "3b3f6010",
        "udid": "192.168.121.103:5555",
        # "appPackage": "com.qaautomation.approved.android.test",
        "appPackage": "com.india.bb.test",
        "autoAcceptAlerts": True,
        "autoGrantPermissions": True,
        "appActivity": "com.bbapp.MainActivity",
    }
    # caps = {}
    # caps["appium:deviceName"] = "Android Emulator"
    # caps["platformName"] = "Android"
    # caps["appium:AppPackage"] = "com.bbqaautomation.android"
    # caps["appium:appWaitActivity"] = "com.bbapp.MainActivity"
    # caps["appium:autoGrantPermissions"] = True
    # caps["appium:uid"] = "3b3f6010"
    # caps["appium:ensureWebviewsHavePages"] = True
    # caps["appium:nativeWebScreenshot"] = True
    # caps["appium:newCommandTimeout"] = 3600
    # caps["appium:connectHardwareKeyboard"] = True

    driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=capabilities)

    return driver

def teardown():

    driver.quit()