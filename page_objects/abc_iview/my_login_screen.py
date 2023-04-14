from appium.webdriver.common.appiumby import AppiumBy

from utilities.application import Application
from page_objects.abc_iview.base_ui import BaseUI

from utilities.read_properties import ReadProperties
from utilities.utils import config


class MyLoginScreen(BaseUI):
    if ReadProperties.getPlatformName() == 'ios':
        log_in_with_email_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="LOG IN WITH EMAIL"]')
        sign_up_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Sign Up"]')
        log_in_btn = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Log in"]')
        sign_up_with_email_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="SIGN UP WITH EMAIL"]')
        email_fld = (AppiumBy.XPATH,
                     '//XCUIElementTypeOther[@name="Log in with email - ABC Account - ABC - Australian Broadcasting Corporation"]/XCUIElementTypeTextField')
        password_fld = (AppiumBy.XPATH,
                        '//XCUIElementTypeOther[@name="Log in with email - ABC Account - ABC - Australian Broadcasting Corporation"]/XCUIElementTypeSecureTextField')
        ios_done_key = (AppiumBy.ACCESSIBILITY_ID, "Done")
        continue_to_iview_btn = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="CONTINUE TO IVIEW"]')

    else:
        log_in_with_email_btn = (AppiumBy.XPATH, '//*[@text="LOG IN WITH EMAIL"]')
        sign_up_btn = (AppiumBy.XPATH, '//*[@text="Sign Up"]')
        log_in_btn = (AppiumBy.XPATH, '//*[@text="Log in"]')
        sign_up_with_email_btn = (AppiumBy.XPATH, '//*[@text="SIGN UP WITH EMAIL"]')
        email_fld = (AppiumBy.XPATH, '//*/android.view.View[2]/android.widget.EditText')
        password_fld = (AppiumBy.XPATH, '//*/android.view.View[4]/android.widget.EditText')
        continue_to_iview_btn = (AppiumBy.XPATH, '//*[@text="CONTINUE TO IVIEW"]')

    def __init__(self, app):
        super().__init__(app)

    def clickOniOSDoneKey(self):
        if ReadProperties.getPlatformName() == 'ios':
            if self.is_visible_after_wait(self.ios_done_key, 2):
                self.click(self.ios_done_key)

    def clickOnLoginWithEmailBtn(self, App: Application):
        self.wait_implicit(50)
        actions = App.set_actions()

        if not self.is_visible(self.log_in_with_email_btn):
            self.click(self.sign_up_btn)
            self.click(self.log_in_btn)
            # actions.tap(self.wait_visible(self.sign_up_btn)).perform()
            # actions.tap(self.wait_visible(self.log_in_btn)).perform()

        self.click(self.log_in_with_email_btn)

    def checkContinueToiViewBtnVisible(self):
        try:
            self.wait_visible(self.continue_to_iview_btn)
        except:
            self.logger.warning("Continue To iView Button does not exist. Continue to Sub Profile Screen...")
        return self.is_visible(self.continue_to_iview_btn)