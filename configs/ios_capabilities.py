# Full list of available capabilities here: https://appium.github.io/appium/docs/en/2.0/guides/caps/
import os

from utilities.read_properties import read_config, ReadProperties


def get_ios_capabilities(section_name):
    config = read_config()

    capabilities = {
        "platformName": config.get(section_name, "platform_name"),
        "appium:app": os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'apps', config.get(section_name, "app_name"))),
        "appium:autoAcceptAlerts": True,
        "appium:autoGrantPermissions": True,
        "appium:automationName": "XCuiTest",
        "appium:commandTimeouts": "12000",
        "appium:deviceName": config.get(section_name, "device_name"),
        "appium:platformVersion": config.get(section_name, "platform_version"),
        "appium:udid": config.get(section_name, "udid"),
        "appium:wdaLaunchTimeout": 50000,
        "appium:xcodeOrgId": "purwar.gaurav@abc.net.au",
        "appium:xcodeSigningId": "Developer"
    }

    return capabilities


def get_aws_ios_capabilities():

    capabilities = {
        "usePrebuiltWDA": True,
        "derivedDataPath": os.environ.get("DEVICEFARM_WDA_DERIVED_DATA_PATH"),
        "platformName": os.environ.get("DEVICEFARM_DEVICE_PLATFORM_NAME"),
        "appium:app": os.environ.get("DEVICEFARM_APP_PATH"),
        "appium:autoAcceptAlerts": True,
        "appium:autoGrantPermissions": True,
        "appium:automationName": "XCUITest",
        "appium:commandTimeouts": 12000,
        "appium:deviceName": os.environ.get("DEVICEFARM_DEVICE_NAME"),
        "appium:platformVersion": os.environ.get("DEVICEFARM_DEVICE_OS_VERSION"),
        "appium:udid": os.environ.get("DEVICEFARM_DEVICE_UDID_FOR_APPIUM"),
        "appium:wdaLaunchTimeout": 50000,
        "appium:newCommandTimeout": 40000,
        "appium:xcodeOrgId": "purwar.gaurav@abc.net.au",
        "appium:xcodeSigningId": "Developer"
    }

    return capabilities
