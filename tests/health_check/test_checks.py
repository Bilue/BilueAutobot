from tests.health_check.base_tests import BaseTests


class TestChecks(BaseTests):

    def test_001_check_loggers(self, App):
        try:
            self.logger.info("*************** Test_Check_001 *****************")

        except Exception as e:
            self.handle_exception(App, e)

    def test_002_check_assertions(self, App):
        try:
            self.init_test(App)
            self.logger.info("*************** Test_Check_002 *****************")
            self.soft_assert.assert_true(True, "True Assertion Should be Performed!")
            self.soft_assert.assert_all()

        except Exception as e:
            self.handle_exception(App, e)

    def test_003_check_api_calls(self, App):
        try:
            self.init_test(App)
            self.logger.info("*************** Test_Check_003 *****************")
            try:
                self.linktv_screen.link_tv_with_abc_account(self.ctv_login_url, self.ctv_verify_url, self.api_key, self.user_email, self.password)
            except:
                self.logger.info("API will work with valid URL and API Key")

        except Exception as e:
            self.handle_exception(App, e)

    def test_004_check_web_browser_title(self, App):
        try:
            self.init_test(App)
            self.logger.info("*************** Test_Check_003 *****************")
            self.logger.info("Website Title"+str(App.driver_instance.title))

        except Exception as e:
            self.handle_exception(App, e)
