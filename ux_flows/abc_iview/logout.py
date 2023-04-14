from utilities.application import Application
from ux_flows.abc_iview.base_screen_action import BaseScreenAction
from page_objects.abc_iview.my_account_profile import MyAccountProfile


class LogoutFlow(BaseScreenAction):

    def __init__(self, app):
        super().__init__(app)

    def logout_steps(self, App: Application):
        myAccountProfile = MyAccountProfile(app=App)

        # logout iview app
        myAccountProfile.clickMyAccountProfileBtn()
        myAccountProfile.clickLogoutOfIviewBtn()
