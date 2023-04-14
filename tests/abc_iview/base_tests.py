import inspect
import pytest

from utilities.custom_logger import LogGen
from utilities.application import Application
from utilities.read_properties import ReadProperties

from utilities.utils import Utils, config

"""
This is a Python script for a set of base test classes. It includes the following features:

*Reading email and password from a properties file using the ReadProperties class.
*Logging information using the LogGen class to log errors and debug information.
*Taking screenshots of the application in case of an error using the ScreenshotManager and Utils classes.
*Implementing fixtures to initialize and close the application using the MyApplication class.
*A handle_exception method that captures and logs exceptions thrown during test execution, and takes a screenshot.
*A tearDown method to close the application after the tests have finished executing.

This script will be used as a base for test cases for a mobile application, with each test case class inheriting from 
the BaseTests class.

@Author Gaurav Purwar

"""


class ScreenshotManager:
    scr = []


class BaseTests:
    email = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = LogGen.loggen()

    def init_test(self, App: Application):
        from ux_flows.abc_iview.login import LoginFlow
        from ux_flows.abc_iview.logout import LogoutFlow
        from ux_flows.abc_iview.profile import Profile
        from page_objects.abc_iview.home_screen import HomeScreen
        from page_objects.abc_iview.iview_login_screen import Iview_Login_Screen
        from page_objects.abc_iview.my_login_screen import MyLoginScreen
        from page_objects.abc_iview.whos_watching_screens import WhosWatchingScreens
        from ux_flows.abc_iview.watchlist import Watchlist
        from page_objects.abc_iview.videoPlayer import VideoPlayerScreen
        from page_objects.abc_iview.watchlist_screen import WatchlistScreen
        from utilities.soft_assert import SoftAssert

        self.soft_assert = SoftAssert()
        self.iview_login = Iview_Login_Screen(app=App)
        self.mylogin_screen = MyLoginScreen(app=App)
        self.loginFlow = LoginFlow(app=App)
        self.profile = Profile(app=App)
        self.watchlist_screen = WatchlistScreen(app=App)
        self.watchlist = Watchlist(app=App)
        self.whosWatchingScreen = WhosWatchingScreens(app=App)
        self.homeScreen = HomeScreen(app=App)
        self.videoPlayer = VideoPlayerScreen(app=App)
        self.logoutFlow = LogoutFlow(app=App)

    def handle_exception(self, app, e):
        utils = Utils(app=app)
        test_class_name = self.__class__.__name__
        test_method_name = [frame[3] for frame in inspect.stack() if frame[3].startswith("test_")][0]
        test_case_name = f"{test_class_name}.{test_method_name}"
        self.logger.error(f"{test_case_name} failed: {e}")
        # ScreenshotManager.scr = utils.saveScreenshot(f"{test_case_name}")
        ScreenshotManager.scr.append(utils.saveScreenshot(f"{test_case_name}"))
        self.logger.error("Handle Exception With Screenshot: " + str(ScreenshotManager.scr))
        raise Exception(f"{test_case_name} failed: {e}")

    @pytest.fixture(scope='class')
    def App(self, request, mobile_devices):
        section_name = request.config.getoption("--device")
        if not section_name:
            section_name = mobile_devices[0]
        ReadProperties.setPlatformName(section_name)

        App = Application()
        self.logger.info("in setup")
        App.set_actions()
        self.logger.info(f"Running Test on Mobile device: {section_name}")
        App.launchApp(section_name)
        screenSize = App.driver_instance.get_window_size()
        self.logger.info("Screen size is: ", screenSize)

        def tearDown():
            self.logger.info("In tearDown")
            App.close_my_application()

        request.addfinalizer(tearDown)

        return App
