import inspect

from utilities.custom_logger import LogGen
from utilities.application import Application
from utilities.read_properties import ReadProperties

from utilities.utils import Utils

"""
    Base class for test cases in the ABC News test automation framework.

    This class provides common functionality and utilities used by test cases.
    It includes methods for initializing test dependencies, handling exceptions, and logging.

    Attributes:
        email (str): The email used for testing.
        password (str): The password used for testing.
        logger: The logger instance for logging purposes.

    Methods:
        init_test(App: Application): Initializes the test dependencies, such as screen objects and flows.
        handle_exception(app, e): Handles exceptions that occur during test execution, captures a screenshot, and raises an exception.

    Usage:
        Inherit from the `BaseTests` class to create test cases in the ABC News test automation framework.
        Implement test methods within the derived test case classes.

    Example:
        class TestLogin(BaseTests):
            def test_login(self, App):
                try:
                    self.init_test(App)
                    # Test case steps...
                except Exception as e:
                    self.handle_exception(App, e)
                    # Handle the exception or failure case
                    
    Author: 
        Gaurav Purwar
    
    Date:     27th July 2023
    """


class ScreenshotManager:
    scr = []


class BaseTests:
    user_email = ReadProperties.get_user_email()
    password = ReadProperties.get_password()
    ctv_login_url = ReadProperties.get_ctv_login_url()
    ctv_verify_url = ReadProperties.get_ctv_verify_url()
    api_key = ReadProperties.get_api_key()
    logger = LogGen.loggen()

    def init_test(self, App: Application):
        from utilities.soft_assert import SoftAssert
        from page_objects.abc_iview_tv.linktv_screen import LinkTvScreen

        self.soft_assert = SoftAssert()
        self.linktv_screen = LinkTvScreen(app=App)

    def handle_exception(self, app, e):
        utils = Utils(app=app)
        test_class_name = self.__class__.__name__
        test_method_name = [frame[3] for frame in inspect.stack() if frame[3].startswith("test_")][0]
        test_case_name = f"{test_class_name}.{test_method_name}"
        self.logger.error(f"{test_case_name} failed: {e}")
        ScreenshotManager.scr.append(utils.saveScreenshot(f"{test_case_name}"))
        self.logger.error("Handle Exception With Screenshot: " + str(ScreenshotManager.scr))
        raise Exception(f"{test_case_name} failed: {e}")

