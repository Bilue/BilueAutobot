# Full list of available capabilities here: https://appium.github.io/appium/docs/en/2.0/guides/caps/
import configparser
import os

from utilities.read_properties import read_config, ReadProperties

Apps_Path = os.path.abspath('../mobile-automation-tests/apps/ABC-iview1901202311.app.zip')


def getiOSCapabilities(section_name):
    config = read_config()

    capabilities = {
        "platformName": config.get(section_name, "platform_name"),
        "appium:app": f"{Apps_Path}",
        "appium:autoAcceptAlerts": True,
        "appium:autoGrantPermissions": True,
        "appium:automationName": "XCuiTest",
        "appium:commandTimeouts": "12000",
        "appium:deviceName": config.get(section_name, "deviceName"),
        "appium:platformVersion": config.get(section_name, "platformVersion"),
        "appium:udid": config.get(section_name, "udid"),
        "appium:wdaLaunchTimeout": 50000,
        "appium:xcodeOrgId": "gaurav.purwar@bilue.com.au",
        "appium:xcodeSigningId": "Developer"
    }

    return capabilities
