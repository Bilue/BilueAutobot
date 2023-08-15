import pytest
from appium.webdriver.common.appiumby import AppiumBy

from page_objects.abc_iview_tv.base_ui import BaseUI
from utilities.read_properties import ReadProperties


class LaunchScreen(BaseUI):
    if ReadProperties.get_platform_name() == 'tvOS':
        tv_login_easy_get_started_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="EASY, GET STARTED"]')

    elif ReadProperties.get_platform_name() == 'Android':
        package_name = ReadProperties.get_package_name()
        tv_login_easy_get_started_btn = (AppiumBy.ID, f'{package_name}:id/loginToWatchButton')
        tv_login_header_text = (AppiumBy.ID, f'{package_name}:id/onBoardingHeaderTextView')#Watch ABC iview for free. Anytime, anywhere.
        tv_login_onboarding_text = (AppiumBy.ID, f'{package_name}:id/onBoardingMessageTextView')#Create profiles, save your favourites and pick up where you left off with an ABC Account.
        tv_login_info_btn = (AppiumBy.ID, f'{package_name}:id/infoButton')
        tv_login_learn_more_info_txt = (AppiumBy.ID, f'{package_name}:id/learnMoreTextView')#Learn about an ABC Account, and Privacy at the ABC: abc.net.au/iviewlogin

    else:
        pytest.fail("ERROR - Check the Platform Name: " + str(ReadProperties.get_platform_name()))

    def __init__(self, app):
        super().__init__(app)

