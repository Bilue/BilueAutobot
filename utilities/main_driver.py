from appium import webdriver
from appium.options.ios.xcuitest.base import XCUITestOptions
from appium.options.android.uiautomator2.base import UiAutomator2Options
from configs.android_capabilities import getAndroidCapabilities
from configs.ios_capabilities import getiOSCapabilities
from utilities.read_properties import ReadProperties

"""
The class MainDriver is a Python class that provides functionality for opening a mobile application on either 
Android or iOS platforms. The class makes use of the Appium library for launching the application, 
with the appropriate platform-specific capabilities. The class provides methods for opening an application for either 
platform, updating the driver for interacting with Jetpack Compose UI elements on Android or normal UI elements on 
Android, and closing the application. The class uses the ReadProperties class to determine the platform on which the 
application should be launched. The class is designed to be used as a parent class in a larger framework for 
automating mobile applications.

@author Gaurav Purwar

"""


class MainDriver():
    def __init__(self):
        self.driver_instance = None

    def launchApp(self, section_name):
        if 'ios' in section_name.lower():
            self.open_application_ios(section_name)
        elif 'android' in section_name.lower():
            self.open_application_android(section_name)
        else:
            raise ValueError("Please check the device in command line argument: "+str(section_name))

    def open_application_android(self, section_name):
        cap = getAndroidCapabilities(section_name)
        options = UiAutomator2Options().load_capabilities(cap)
        driver = webdriver.Remote(command_executor=ReadProperties.getAppiumSessionUrl(), options=options)
        self.driver_instance = driver
        return driver

    def open_application_ios(self, section_name):
        cap = getiOSCapabilities(section_name)
        options = XCUITestOptions().load_capabilities(cap)
        driver = webdriver.Remote(command_executor=ReadProperties.getAppiumSessionUrl(), options=options)
        self.driver_instance = driver
        return driver

    def update_driver_to_Compose(self):
        """
        In order to interact Jetpack Compose UI elements, we need to change driver setting to handle Compose UI.
        Use for updating driver setting to Compose, this is for handling Jetpack Compose UI elements on Android only

        Usage: App.update_driver_to_Compose()
        """
        Current_Session_cap = self.driver_instance.capabilities
        if Current_Session_cap['platformName'] == "iOS":
            raise ValueError(
                "Invalid platformName, this update driver setting supports only Android, the current driver is: ",
                Current_Session_cap['platformName'])
        try:
            print("Current Setting is...", self.driver_instance.get_settings())
            self.driver_instance.update_settings({"driver": "compose"})
            print("After Setting is...", self.driver_instance.get_settings())
        except:
            raise ValueError("Could not update driver setting, please check driver_instance: ", self.driver_instance)

    def update_driver_to_Espresso(self):
        """
        Use for updating driver setting to Espresso, this is for handling normal (not compose) UI elements on Android only.

        Usage: App.update_driver_to_Espresso()
        """
        Current_Session_cap = self.driver_instance.capabilities
        if Current_Session_cap['platformName'] == "iOS":
            raise ValueError(
                "Invalid platformName, this update driver setting supports only Android, the current driver is: ",
                Current_Session_cap['platformName'])
        try:
            self.driver_instance.update_settings({"driver": "espresso"})
        except:
            raise ValueError("Could not update driver setting, please check driver_instance: ", self.driver_instance)

    def close_application(self):
        self.driver_instance.quit()
