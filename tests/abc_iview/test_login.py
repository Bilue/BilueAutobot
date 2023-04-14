from tests.abc_iview.base_tests import BaseTests


class TestLogin(BaseTests):

    """
    test_login_flow_001: when user is not logged in
    """
    def test_login_flow_001(self, App):
        try:
            self.init_test(App)
            self.logger.info("*************** Test_Login_001 *****************")
            # Start
            assert self.iview_login.is_visible_after_wait(self.iview_login.log_in_to_watch_btn) == True, "#####Login to Watch Button is not visible on Onboarding Screen"
            self.iview_login.clickOnLoginToWatchBtn()
            # Perform Login Steps

            assert self.mylogin_screen.is_visible_after_wait(self.mylogin_screen.log_in_with_email_btn) == True, "#####Login with Email Button is not visible on Login Screen"
            self.mylogin_screen.clickOnLoginWithEmailBtn(App)

            assert self.mylogin_screen.is_visible_after_wait(self.mylogin_screen.email_fld) == True, "#####Email Field is not visible on Login Screen"
            self.mylogin_screen.send_keys(self.mylogin_screen.email_fld, self.email)

            assert self.mylogin_screen.is_visible_after_wait(self.mylogin_screen.password_fld) == True, "#####Password Field is not visible on Login Screen"
            self.mylogin_screen.send_keys(self.mylogin_screen.password_fld, self.password)
            self.mylogin_screen.clickOniOSDoneKey()

            assert self.mylogin_screen.is_visible_after_wait(self.mylogin_screen.log_in_with_email_btn, 50) == True, "#####Login with Email Button is not visible on Login Screen"
            self.mylogin_screen.click(self.mylogin_screen.log_in_with_email_btn)

            if not self.whosWatchingScreen.verifyTitleVisible(10):
                self.mylogin_screen.click(self.mylogin_screen.continue_to_iview_btn)
            assert self.whosWatchingScreen.is_visible_after_wait(self.whosWatchingScreen.whos_watching_title) == True, "#####Title is not visible on Login Screen"
            self.logger.info("**** Logged in Successfully ****")

        except Exception as e:
            self.handle_exception(App, e)

    """
    test_login_profile_002: when user is already logged in either after test_login_flow_001 execution or by default logged in
    """
    def test_login_profile_002(self, App):
        try:
            self.init_test(App)
            self.logger.info("*************** Test_Login_002 *****************")
            assert self.whosWatchingScreen.verifyTitleVisible() == True, "#######Title not visible on Who's Watching Screen"
            self.logger.info("**** Who's Watching Screen Title Verified Successfully ****")

            # Choose Sub Profile
            self.whosWatchingScreen.clickOnMainProfileBtn()

            # Logout
            self.logoutFlow.logout_steps(App)
            self.logger.info("****Successfully Logged out!!! ****")

        except Exception as e:
            self.handle_exception(App, e)
