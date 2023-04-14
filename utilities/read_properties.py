import os
from pathlib import Path
import configparser

from utilities.custom_logger import LogGen


def read_config():
    path = Path(__file__)
    ROOT_DIR = path.parent.absolute().parent
    config_path = os.path.join(ROOT_DIR, "Configs/config.ini")
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


"""This script reads values from a configuration file located at "Configs/config.ini". The script 
contains a class named "ReadProperties" which has four static methods:

*getPlatformName(): returns the value of the "platform" field under the section "common info" in the configuration file.
*getUserEmail(): returns the value of the "useremail" field under the section "common info" in the configuration file.
*getPassword(): returns the value of the "password" field under the section "common info" in the configuration file.
*getSubProfile(): returns the value of the "subprofileName" field under the section "common info" in the configuration file.

@author Gaurav Purwar
"""


class ReadProperties:
    platform_name = None

    @staticmethod
    def getPlatformName():
        return ReadProperties.platform_name

    @staticmethod
    def getUserEmail():
        email = read_config().get('common info', 'useremail')
        return email

    @staticmethod
    def getPassword():
        password = read_config().get('common info', 'password')
        return password

    @staticmethod
    def getSubProfile():
        subProfile = read_config().get('common info', 'subprofileName')
        return subProfile

    @staticmethod
    def getiOSWaitTime():
        iosWait = read_config().get('common info', 'iosWaitTime')
        return int(iosWait)

    @staticmethod
    def getAndroidWaitTime():
        androidWait = read_config().get('common info', 'androidWaitTime')
        return int(androidWait)

    @staticmethod
    def getAppiumSessionUrl():
        appiumSession = read_config().get('common info', 'appiumSessionUrl')
        return appiumSession

    # for section in config.sections():
    #     if section.startswith('Android'):
    #         platform_name = config.get(section, 'platformName')
    #         # platform_version = config.get(section, 'platformVersion')
    #         device_name = config.get(section, 'deviceName')
    #         # do something with the Android device properties
    #
    #     elif section.startswith('iOS'):
    #         platform_name = config.get(section, 'platformName')
    #         platform_version = config.get(section, 'platformVersion')
    #         device_name = config.get(section, 'deviceName')
    #         # do something with the iOS device properties
    @staticmethod
    def setPlatformName(section_name):
        logger = LogGen.loggen()
        platform_name = read_config().get(section_name, 'platform_name')
        logger.info(f" Setting Platform Name as : {platform_name}")
        ReadProperties.platform_name = platform_name
