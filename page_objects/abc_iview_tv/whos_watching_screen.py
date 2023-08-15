import pytest
from appium.webdriver.common.appiumby import AppiumBy

from page_objects.abc_iview_tv.base_ui import BaseUI
from utilities.read_properties import ReadProperties


class WhosWatchingScreen(BaseUI):
    if ReadProperties.get_platform_name() == 'tvOS':
        tv_wws_title = (AppiumBy.ACCESSIBILITY_ID, 'Who’s watching?')

    elif ReadProperties.get_platform_name() == 'Android':
        tv_wws_title = (AppiumBy.ID, 'au.net.abc.iview:id/profileTitle')

    else:
        pytest.fail("ERROR - Check the Platform Name: " + str(ReadProperties.get_platform_name()))

    def __init__(self, app):
        super().__init__(app)

