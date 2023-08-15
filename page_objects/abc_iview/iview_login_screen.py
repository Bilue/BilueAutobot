from appium.webdriver.common.appiumby import AppiumBy

from utilities.application import Application
from page_objects.abc_iview.base_ui import BaseUI

from utilities.read_properties import ReadProperties
from utilities.utils import config


class Iview_Login_Screen(BaseUI):
    if ReadProperties.get_platform_name() == 'ios':
        log_in_to_watch_btn = (AppiumBy.ACCESSIBILITY_ID, 'LOG IN TO WATCH')

    else:
        log_in_to_watch_btn = (AppiumBy.ID, 'au.net.abc.iview:id/buttonGetStarted')

    def __init__(self, app):
        super().__init__(app)

    def iview_login_btn(self):
        iview_login_btn_element = self.app.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                                        value="LOG IN TO WATCH")
        assert iview_login_btn_element.is_displayed() == True
        assert iview_login_btn_element.text == "LOG IN TO WATCH"
        assert iview_login_btn_element.is_enabled() == True
        return iview_login_btn_element

    def iview_login_title(self):
        iview_login_title_element = self.app.driver_instance.find_element(by=AppiumBy.XPATH,
                                                                          value='//XCUIElementTypeStaticText[@name="Watch ABC iview for free. Anytime, anywhere."]')
        assert iview_login_title_element.text == "Watch ABC iview for free. Anytime, anywhere."
        assert iview_login_title_element.is_displayed() == True
        assert iview_login_title_element.is_enabled() == True
        return iview_login_title_element

    def iview_login_description(self):
        iview_login_description = self.app.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                                        value="Create profiles, save your favourites and pick up where you left off with an ABC Account.")
        assert iview_login_description.is_displayed() == True
        assert iview_login_description.is_enabled() == True
        return iview_login_description

    def iview_login_info(self):
        iview_login_info = self.app.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                                 value="Tell me more about ABC Accounts")
        assert iview_login_info.is_displayed() == True
        assert iview_login_info.is_enabled() == True
        return iview_login_info

    def iview_login_privacy(self):
        iview_login_privacy = self.app.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                                    value="Privacy at the ABC")
        assert iview_login_privacy.is_displayed() == True
        assert iview_login_privacy.is_enabled() == True
        return iview_login_privacy

    def clickOnLoginBtn(self, App: Application):
        actions = App.set_actions()
        actions.tap(self.iview_login_btn()).perform()

    def clickOnLoginToWatchBtn(self):
        self.click(self.log_in_to_watch_btn)

    def verifyLoginToWatchBtnVisible(self):
        self.wait_visible(self.log_in_to_watch_btn)
        return self.is_visible(self.log_in_to_watch_btn)