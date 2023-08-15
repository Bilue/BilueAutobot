from enum import Enum

from selenium.webdriver import ActionChains

from utilities.main_driver import MainDriver
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadProperties
from utilities.utils import Utils, TVRemoteAction
from utilities.api_utils import APIUtility


class BaseUI(ActionChains):
    """
    Base class for UI-related functionality in the test automation framework.

    This class provides common methods and utilities for interacting with the user interface.
    It extends the `ActionChains` class, allowing for performing actions like mouse movements and interactions.

    Attributes:
        app (MainDriver): The main driver instance representing the application under test.
        logger: The logger instance for logging purposes.
        utils (Utils): An instance of the Utils class providing utility methods for UI interactions.
    Author:
        Gaurav Purwar

    Date:     27th July 2023

    """
    app = None
    logger = LogGen.loggen()
    platform_name = ReadProperties.get_platform_name()

    def __init__(self, app: MainDriver):
        self.app = app
        self.utils = Utils(app)
        self.api_utils = APIUtility()

    def get_element(self, locator):
        return self.utils.get_element(locator)

    def get_attribute(self, locator, attribute: str):
        element = self.get_element(locator)
        return element.get_attribute(attribute)

    def get_elements(self, locator):
        return self.utils.get_elements(locator)

    def press_key(self, button_name):
        self.utils.tv_remote_control(button_name)

    def press_enter(self, locator=None, element=None):
        platform_name = ReadProperties.get_platform_name()
        if platform_name == 'tvOS':
            self.press_key(TVRemoteAction.ENTER)
        else:
            self.click(locator, element)

    def click(self, locator=None, element=None):
        self.utils.click(locator, element)
        if locator is not None:
            self.logger.info("***************" + str(locator[1]) + " Button clicked")
        else:
            self.logger.info("***************Element clicked")

    def swipe_down(self, locator, timeout):
        self.utils.swipe_down(locator=locator, timeout=timeout)

    def is_visible_after_wait(self, locator, timeout=None):
        try:
            self.utils.wait_visible(locator, timeout=timeout)
            self.logger.info("*************** Wait for element visible performed")
            return True
        except Exception as e:
            self.logger.warning("*************** Element Not visible: " + str(e))
            return False
