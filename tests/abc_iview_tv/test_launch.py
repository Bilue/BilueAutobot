from tests.abc_iview_tv.base_tests import BaseTests


class TestLaunch(BaseTests):

    def test_001_onboarding_screen_validation(self, App):
        try:
            self.init_test(App)
            self.logger.info("*************** Test_Login_001 *****************")
            self.soft_assert(
                self.launch_screen.is_visible_after_wait(self.launch_screen.tv_login_easy_get_started_btn),
                "Easy, Get Started button on onboarding screen should be visible")

        except Exception as e:
            self.handle_exception(App, e)

    def test_002_onboarding_screen_functional_validation(self, App):
        try:
            self.init_test(App)
            self.logger.info("*************** Test_Login_002 *****************")

            self.launch_screen.press_enter(locator=self.launch_screen.tv_login_easy_get_started_btn)
            self.soft_assert(self.linktv_screen.is_visible_after_wait(self.linktv_screen.tv_link_tv_scan_qr_1_website_title), "Title 1 on Link TV screen should be visible")

        except Exception as e:
            self.handle_exception(App, e)

