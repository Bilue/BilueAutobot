# Full list of available capabilities here: https://appium.github.io/appium/docs/en/2.0/guides/caps/
import os

from utilities.read_properties import read_config

Apps_Path = os.path.abspath('../mobile-automation-tests/apps/mobile-production-debug.apk')


def getAndroidCapabilities(section_name):
    config = read_config()

    capabilities = {
        "platformName": config.get(section_name, "platform_name"),
        "appium:automationName": "uiautomator2",
        "appium:deviceName": config.get(section_name, "deviceName"),
        "appium:app": f"{Apps_Path}",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:showGradleLog": "true",
        "appium:full_reset": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:espressoBuildConfig": "{\"additionalAndroidTestDependencies\": [\"androidx.lifecycle:lifecycle-extensions:2.2.0\", \"androidx.activity:activity:1.3.1\",  \"androidx.fragment:fragment:1.3.5\"]}"
    }
    return capabilities
