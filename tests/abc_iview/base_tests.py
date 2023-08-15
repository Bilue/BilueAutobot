import inspect
from utilities.custom_logger import LogGen
from utilities.application import Application
from utilities.read_properties import ReadProperties

from utilities.utils import Utils

"""
    Base class for test cases in the ABC iview test automation framework.

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
    """


class ScreenshotManager:
    scr = []


class BaseTests:
    email = ReadProperties.get_user_email()
    password = ReadProperties.get_password()
    logger = LogGen.loggen()

    def init_test(self, App: Application):
        from ux_flows.abc_iview.login import LoginFlow
        from ux_flows.abc_iview.logout import LogoutFlow
        from page_objects.abc_iview.iview_login_screen import Iview_Login_Screen
        from page_objects.abc_iview.my_login_screen import MyLoginScreen
        from page_objects.abc_iview.whos_watching_screens import WhosWatchingScreens
        from page_objects.abc_iview.my_account_profile_screen import MyAccountProfileScreen
        from page_objects.abc_iview.videoPlayer import VideoPlayerScreen
        from utilities.soft_assert import SoftAssert

        self.soft_assert = SoftAssert()
        self.iview_login = Iview_Login_Screen(app=App)
        self.mylogin_screen = MyLoginScreen(app=App)
        self.loginFlow = LoginFlow(app=App)
        self.whos_watching_screen = WhosWatchingScreens(app=App)
        self.my_account_profile_screen = MyAccountProfileScreen(app=App)
        self.videoPlayer = VideoPlayerScreen(app=App)
        self.logoutFlow = LogoutFlow(app=App)

    def handle_exception(self, app, e):
        utils = Utils(app=app)
        test_class_name = self.__class__.__name__
        test_method_name = [frame[3] for frame in inspect.stack() if frame[3].startswith("test_")][0]
        test_case_name = f"{test_class_name}.{test_method_name}"
        self.logger.error(f"{test_case_name} failed: {e}")
        ScreenshotManager.scr.append(utils.saveScreenshot(f"{test_case_name}"))
        self.logger.error("Handle Exception With Screenshot: " + str(ScreenshotManager.scr))
        raise Exception(f"{test_case_name} failed: {e}")