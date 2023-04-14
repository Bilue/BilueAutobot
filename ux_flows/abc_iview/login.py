from page_objects.abc_iview.whos_watching_screens import WhosWatchingScreens
from utilities.application import Application
from utilities.custom_logger import LogGen
from ux_flows.abc_iview.base_screen_action import BaseScreenAction
from page_objects.abc_iview.my_login_screen import MyLoginScreen

'''
Author: Gaurav Purwar
Class: 
This code defines a class LoginActions that performs login steps for an application called MyApplication. The 
class inherits from BaseScreenAction, and the login_steps method takes an instance of MyApplication and a user's 
email and password as inputs. 

Methods: 
The method creates an instance of MyLoginScreen and performs a series of clicks and 
data input actions to complete the login process. It also checks if a "Continue to iView" button is visible and 
clicks on it if so.'''


class LoginFlow(BaseScreenAction):
    logger = LogGen.loggen()

    def __init__(self, app):
        super().__init__(app)

    def login_steps(self, App: Application, email, password):
        mylogin_screen = MyLoginScreen(app=App)
        whosWatchingScreen = WhosWatchingScreens(app=App)

        # Login via Browser
        mylogin_screen.clickOnLoginWithEmailBtn(App)
        mylogin_screen.send_keys(mylogin_screen.email_fld, email)
        mylogin_screen.send_keys(mylogin_screen.password_fld, password)
        mylogin_screen.clickOniOSDoneKey()
        mylogin_screen.click(mylogin_screen.log_in_with_email_btn)
        if not whosWatchingScreen.verifyTitleVisible():
            mylogin_screen.click(mylogin_screen.continue_to_iview_btn)

        self.logger.info("Login Successful!")

        # Refer to Who'sWatchingScreen class to choose sub profile
