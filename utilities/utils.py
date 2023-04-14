import os
from datetime import time, datetime
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, WebDriverException, InvalidSessionIdException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from utilities.main_driver import MainDriver
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadProperties, read_config

"""
    @Author: Gaurav Purwar
    
    SwipeDirection Utils The class uses Selenium and Appium to find elements on the mobile app's user interface. This 
    code defines a class SwipeDirection with two class variables Up and Down. It also defines a class Utils that 
    performs utility functions for an app called MainDriver. The Utils class has a logger and an instance variable 
    app that is initialized in the constructor.
    
    
    The class provides a get_element method that returns an element based on a provided locator. The locator is a tuple 
    with the first element being the method to use for finding the element and the second element being the locator 
    value. If the locator value is a string, the method get_element_by_type is called with the method and value. If the 
    locator value is a list, the method iterates over the values and tries to find the element using get_element_by_type. 
    If none of the values can find the element, a NoSuchElementException is raised.

"""
config = read_config()


class SwipeDirection():
    Up = "Up"
    Down = "Down"


class Utils:
    logger = LogGen.loggen()

    def __init__(self, app: MainDriver):
        super().__init__()
        self.app = app

    # get elements
    # posts_icon = ('accessibility_id', 'Posts') > Sample Locator Value
    def get_element(self, locator):
        """
        Returns element based on provided locator.
        Locator include the method and locator value in a tuple.
        :param locator:
        :return:
        """

        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_element_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_attribute(self, locator, attribute):
        return self.get_element(locator).get_attribute(attribute)

    def get_element_by_type(self, method, value):
        """
        This is a Python function that finds an element on a mobile app's user interface using Appium. The method of
        finding the element is specified by the method argument, which can be one of the following:

        accessibility_id android ios class_name id xpath name The value argument specifies the search criteria for
        the element. If the specified method is not recognized, the function raises an "Invalid locator method."
        exception. If the element is not found, the function raises an "Element Not Found" exception with details
        about the method and search criteria used.

        :param method:
        :param value:
        :return:
        """
        try:
            if method == AppiumBy.ACCESSIBILITY_ID:
                return self.app.driver_instance.find_element(AppiumBy.ACCESSIBILITY_ID, value)
            elif method == AppiumBy.ANDROID_UIAUTOMATOR:
                return self.app.driver_instance.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                             'new UiSelector().%s' % value)
            elif method == AppiumBy.IOS_UIAUTOMATION:
                return self.app.driver_instance.find_element(AppiumBy.IOS_UIAUTOMATION, value)
            elif method == AppiumBy.CLASS_NAME:
                return self.app.driver_instance.find_element(AppiumBy.CLASS_NAME, value)
            elif method == AppiumBy.ID:
                return self.app.driver_instance.find_element(AppiumBy.ID, value)
            elif method == AppiumBy.XPATH:
                return self.app.driver_instance.find_element(AppiumBy.XPATH, value)
            elif method == AppiumBy.NAME:
                return self.app.driver_instance.find_element(AppiumBy.NAME, value)
            else:
                raise Exception('Invalid locator method.')
        except:
            raise Exception('Element Not Found, method: ' + method + " & locator: " + value)

    def get_elements(self, locator):
        """
        Returns element based on provided locator.
        Locator include the method and locator value in a tuple.
        :param locator:
        :return:
        """

        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_elements_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_elements_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_elements_by_type(self, method, value):
        """
        Refer get_element_by_type
        :param method:
        :param value:
        :return:
        """
        try:
            if method == AppiumBy.ACCESSIBILITY_ID:
                return self.app.driver_instance.find_elements(AppiumBy.ACCESSIBILITY_ID, value)
            elif method == AppiumBy.ANDROID_UIAUTOMATOR:
                return self.app.driver_instance.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              'new UiSelector().%s' % value)
            elif method == AppiumBy.IOS_UIAUTOMATION:
                return self.app.driver_instance.find_elements(AppiumBy.IOS_UIAUTOMATION, value)
            elif method == AppiumBy.CLASS_NAME:
                return self.app.driver_instance.find_elements(AppiumBy.CLASS_NAME, value)
            elif method == AppiumBy.ID:
                return self.app.driver_instance.find_elements(AppiumBy.ID, value)
            elif method == AppiumBy.XPATH:
                return self.app.driver_instance.find_elements(AppiumBy.XPATH, value)
            elif method == AppiumBy.NAME:
                return self.app.driver_instance.find_elements(AppiumBy.NAME, value)
            else:
                raise Exception('Invalid locator method.')
        except:
            raise Exception(
                'Failed to find the locator in the list of elements, method: ' + method + " & locator: " + value)

    # element visible
    def is_visible(self, locator):
        els = self.get_elements(locator)
        if len(els) != 0:
            if els[0].is_displayed():
                self.logger.info("Verified Element Present: " + locator[1])
                return True
            else:
                return False
        else:
            return False

    # TODO to make it global timeouts for ios and android and set timeout for explicit elements
    def wait_visible(self, locator, timeout=None):
        """
        This is a Python function that waits for an element to become visible on a mobile app's user interface using
        Appium. The element's location is specified by the locator argument, which is a tuple containing two values:
        the method for finding the element (e.g., accessibility_id, class_name, etc.) and the search criteria (e.g.,
        'button1', 'input_field', etc.).

        The function repeatedly calls the is_visible() method, which checks if the element is currently visible on
        the screen, until the element becomes visible or the timeout value is reached. The timeout value depends on
        the platform being used, either 2 seconds for iOS or 1000 for Android. If the element is never visible,
        the function raises an exception indicating that the element never became visible, including the method and
        search criteria used.

        :param timeout:
        :param locator:
        :return:
        """
        i = 0
        platform_name = ReadProperties.getPlatformName()
        if timeout is None:
            if platform_name == 'ios':
                timeout = ReadProperties.getiOSWaitTime()
            else:
                timeout = ReadProperties.getAndroidWaitTime()

        self.logger.warning(" Wait Timeout Cycle is: " + str(timeout))

        while i != timeout:
            try:
                if not self.is_visible(locator):
                    self.logger.info(str(i) + " Checking for element " + locator[1])
                else:
                    self.logger.info(str(i) + " element visible: " + locator[1])
                    return self.get_element(locator)
            except NoSuchElementException as e:
                self.logger.error("Error occurred while finding element: %s", str(e))
                sleep(0.1)
            i += 1
        raise Exception('Element never became visible: %s (%s)' % (locator[0], locator[1]))

    # save Screenshot
    def saveScreenshot(self, tcName):
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        file_name = tcName + "_screenshot_{}.png".format(timestamp)
        self.app.driver_instance.get_screenshot_as_file("Screenshots/" + file_name)
        current_dir = os.getcwd()
        screenshot_path = current_dir + "/Screenshots/" + file_name
        return screenshot_path
        # self.app.driver_instance.get_screenshot_as_file("Screenshots/screenshot.png")

    # clicks and taps
    def click(self, locator=None, element=None):
        if element is not None:
            element.click()
            self.logger.info(f"Clicked on element {str(element)}")
        elif locator is not None:
            element = self.wait_visible(locator)
            element.click()
            self.logger.info(f"Clicked on element {str(locator[1])}")
        else:
            raise ValueError("Either a locator or an element must be provided.")

    def tap(self, locator=None, percentage=1.0):
        if locator is not None:
            element = self.wait_visible(locator)
            location = element.location
            width = element.size['width']
            x = location['x'] + int(width * percentage)
            y = location['y'] + element.size['height'] // 2
            self.logger.warning(
                "x :" + str(x) + " location['x'] :" + str(location['x']) + " width :" + str(width) + " y :" + str(
                    y) + " location['y'] :" + str(location['y']) + " height :" + str(element.size['height']))
            touch_action = TouchAction(self.app.driver_instance)
            touch_action.tap(x=x, y=y).perform()
            self.logger.info("Tapped on element " + locator[1])
        else:
            raise ValueError("A locator must be provided.")

    def hide_keyboard(self):
        try:
            sleep(0.5)
            self.app.driver_instance.hide_keyboard()
        except WebDriverException:
            pass

    def send_keys(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)
        sleep(0.1)

    def set_value(self, locator, text):

        element = self.wait_visible(locator)
        element.clear()
        element.set_value(text)
        sleep(0.1)

    def clear(self, locator):
        element = self.wait_visible(locator)
        element.clear()
        sleep(0.1)

    # TODO common method to scroll in Android & iOS, Fix required as this may break the driver instance and may throw
    #  InvalidSessionIdException
    def swipeDown(self, locator, timeout=None):
        # platformName = ReadProperties.getPlatformName()
        # i = 0
        # while i != timeout:
        #     sleep(0.2)
        #     if not self.is_visible(locator):
        #         if platformName == 'ios':
        #             self.app.driver_instance.swipe(150, 900, 150, 100, 500)
        #         else:
        #             self.app.driver_instance.swipe(500, 1600, 500, 200, 500)
        #         self.logger.info(str(i) + " Scrolling down to check for the element " + locator[1])
        #         sleep(0.2)
        #         i += 1
        #     else:
        #         self.logger.info(str(i) + " Scrolling Stop, the element found " + locator[1])
        #         break

        """Swipes down until the given element is visible."""
        i = 0
        timeout = timeout or 50
        while i < timeout:
            try:
                element = self.app.driver_instance.find_element(*locator)
                if element.is_displayed():
                    break
            except NoSuchElementException:
                pass
            start_y = int(self.app.driver_instance.get_window_size()['height'] * 0.8)
            end_y = int(self.app.driver_instance.get_window_size()['height'] * 0.2)
            start_x = int(self.app.driver_instance.get_window_size()['width'] / 2)
            self.app.driver_instance.swipe(start_x, start_y, start_x, end_y, 2000)
            self.logger.info(str(i) + " Scrolling down to check for the element " + locator[1])
            i += 1
        else:
            raise NoSuchElementException(f"Could not find element during swipe down {locator}")

    # get text
    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text

    def wait_for_element_to_appear(self, locator, timeout=50):
        try:
            WebDriverWait(self.app.driver_instance, timeout=timeout).until(
                expected_conditions.visibility_of_any_elements_located(self.get_element(locator)))
        except Exception as e:
            self.logger.error(
                "Error while performing explicit wait for element " + locator[1] + " for " + str(timeout) + str(e))
        self.logger.info("Explicit Wait for element " + locator[1] + " for " + str(timeout))

    def wait_implicit(self, timeout):
        self.app.driver_instance.implicitly_wait(timeout)
        self.logger.info("Implicit Wait for " + str(timeout))

    def Swipe_by_element(self, start_element: WebElement, end_element: WebElement, velocity=1000):
        # perform the swipe by element
        action = self.app.set_actions()
        action.long_press(el=start_element, duration=velocity).move_to(el=end_element).perform()

    def Swipe_by_coord(self, start_x: int = 0, start_y: int = 0, end_x: int = 0, end_y: int = 0, velocity=1000):

        # validate the given values
        screen_size = self.app.driver_instance.get_window_size()
        screen_height = screen_size['height']
        screen_width = screen_size['width']
        if start_x < 0 or start_y < 0 or start_x > screen_width or start_y > screen_height or end_x > screen_width or end_y > screen_height:
            raise ValueError("Invalid positon value, either x and y has exceeded the screen or is below minimum")

        # set action object and perform Swipe_Up
        action = self.app.set_actions()
        action.long_press(el=None, x=start_x, y=start_y, duration=velocity).move_to(el=None, x=end_x,
                                                                                    y=end_y).release().perform()

    def Swipe(self, Direction: str = SwipeDirection.Up, velocity=1000):
        """
        Will attempt to swipe up by using cording from the centre of the screen
        """
        screen_size = self.app.driver_instance.get_window_size()
        # to fix Invalid positon value, either x and y has exceeded the screen or is below minimum
        center_x = screen_size['width'] / 2
        center_y = screen_size['height'] / 2

        match Direction:
            case SwipeDirection.Up:
                start_x = center_x
                start_y = center_y
                end_x = center_x
                end_y = (center_y * 2)
                return self.Swipe_by_coord(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y,
                                           velocity=velocity)

            case SwipeDirection.Down:
                start_x = center_x
                start_y = center_y
                end_x = center_x
                end_y = (center_y * 0)
                return self.Swipe_by_coord(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y,
                                           velocity=velocity)

        self.logger.info("Swipe performed " + str(Direction))

    def get_list_of_num_from_str(String: str):
        """
        This code defines a function called get_list_of_num_from_str that takes a string as an argument. The function
        splits the string into a list of substrings using the split() method, which by default splits a string into a
        list of words using whitespaces as the separator. Then, it creates a list of integers using a list
        comprehension, where each integer is created from a character in the substrings that is a digit using the
        isdigit() method. Finally, the function returns the list of integers.
        :return:
        """
        num = [int(each_character) for each_character in String.split() if each_character.isdigit()]
        return num

    # def get_toggle_switch_status(self, locator):
    #     """
    #     :param locator:
    #     :return:
    #     """
    #     switch_val = None
    #     platform_name = ReadProperties.getPlatformName()
    #     if platform_name == 'ios':
    #         switch_val = int(self.get_attribute(locator, "value"))
    #     elif platform_name == 'Android':
    #         switch_val_str = self.get_attribute(locator, "content-desc")
    #         switch_val = 0 if 'not' in switch_val_str.lower() else 1
    #     if switch_val == 0:
    #         return False
    #     elif switch_val == 1:
    #         return True
    #     else:
    #         raise ValueError(
    #             "Invalid switch value attribute: " + str(switch_val) + " for the locator :" + str(locator[1]))

    def get_toggle_switch_status(self, locator):
        """
        Gets the current toggle switch status (ON or OFF).

        Parameters:
        - locator: a locator for the toggle switch button.

        Returns:
        - True if the toggle switch is ON.
        - False if the toggle switch is OFF.
        """
        platform_name = ReadProperties.getPlatformName()
        if platform_name == 'ios':
            return bool(int(self.get_attribute(locator, "value")))
        elif platform_name == 'Android':
            switch_val_str = self.get_attribute(locator, "content-desc")
            return 'not' not in switch_val_str.lower()
        else:
            raise ValueError(
                "Invalid platform name: " + platform_name)

    def tap_toggle_switch_button(self, locator, status=False, percentage=1.0):
        """
        This function taps a toggle switch button and verifies that the switch is in the expected state. It takes in a locator, a status, and an optional percentage parameter.
        :param locator:
        :param status: Toggle Status to be set to ON or OFF
        :param percentage: The percentage parameter is an optional parameter that allows the user to tap on a specific percentage of the toggle switch button. It takes in a float value between 0.0 and 1.0, where 0.0 represents the leftmost edge of the button and 1.0 represents the rightmost edge of the button. By default, the percentage is set to 1.0, which means that the function will tap on the rightmost edge of the button. However, if the user wants to tap on a different part of the button, they can specify the desired percentage value when calling the function.
                            For example, if the user wants to tap in the middle of the button, they can pass in a percentage value of 0.5. If the user wants to tap on the left third of the button, they can pass in a percentage value of 0.33.
        :return:
        """
        switch_val = None
        platform_name = ReadProperties.getPlatformName()
        if platform_name == 'ios':
            switch_val = int(self.get_attribute(locator, "value"))
        elif platform_name == 'Android':
            switch_val_str = self.get_attribute(locator, "content-desc")
            switch_val = 0 if 'not' in switch_val_str.lower() else 1

        if status:
            if switch_val == 0:
                self.tap(locator, percentage)
            elif switch_val == 1:
                self.logger.info("Toggle Switch is Already ON!")
        else:
            if switch_val == 0:
                self.logger.info("Toggle Switch is Already OFF!")
            elif switch_val == 1:
                self.tap(locator, percentage)
            else:
                raise ValueError(
                    "Check the switch value attribute: " + str(switch_val) + " for the locator :" + str(locator[1]))

        if self.get_toggle_switch_status(locator) != status:
            raise ValueError(
                "Toggle Switch state could not be changed to " + str(status) + " current value :" + str(
                    switch_val) + " for the locator :" + str(locator[1]))
        else:
            self.logger.info(
                "Toggle is set to :" + str(status) + "::" + str(switch_val) + " for the locator :" + str(locator[1]))
