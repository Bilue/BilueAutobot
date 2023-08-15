import pytest
from appium.webdriver.common.appiumby import AppiumBy

from page_objects.abc_iview.base_ui import BaseUI
from utilities.read_properties import ReadProperties
from utilities.utils import config


class MyAccountProfileScreen(BaseUI):
    if ReadProperties.get_platform_name() == 'ios':
        myaccount_profile_btn = (AppiumBy.ACCESSIBILITY_ID, 'loginButton')
        switch_profile_btn = (AppiumBy.ACCESSIBILITY_ID, 'Switch profile')
        manage_ABC_account_btn = (AppiumBy.ACCESSIBILITY_ID, 'Manage ABC Account')
        logout_of_iview_btn = (AppiumBy.NAME, 'Logout')
        cancel_btn = (AppiumBy.NAME, 'Cancel')

    elif ReadProperties.get_platform_name() == 'Android':
        myaccount_profile_btn = (AppiumBy.ACCESSIBILITY_ID, 'My account')
        switch_profile_btn = (AppiumBy.XPATH, '//*[@text= "Switch profile"]')
        manage_ABC_account_btn = (AppiumBy.XPATH, '//*[@text="Manage ABC account"]')
        logout_of_iview_btn = (AppiumBy.XPATH, '//*[@text="Logout of iview"]')

    else:
        pytest.fail("ERROR  - Check the Platform Name: " + str(ReadProperties.get_platform_name()))

    def clickMyAccountProfileBtn(self):
        self.click(self.myaccount_profile_btn)

    def clickLogoutOfIviewBtn(self):
        self.click(self.logout_of_iview_btn)
