import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException

from page_objects.abc_iview.base_ui import BaseUI
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadProperties
from utilities.utils import config


class WhosWatchingScreens(BaseUI):
    SUBPROFILE_NAME = ReadProperties.get_sub_profile()
    POLICY_TEXT = "The ABC Account holder must ensure each profile holder agrees to the ABC Terms of Use, ABC Privacy Collection Statement and ABC Privacy Policy"

    if ReadProperties.get_platform_name() == 'ios':
        # Who's watching screen
        wws_whos_watching_title = (AppiumBy.ACCESSIBILITY_ID, "Who’s watching?")
        WWS_SUBPROFILE_NAME_XPATH = f'//*[contains(@name,"{SUBPROFILE_NAME}")]'
        wws_subprofile_btn = (AppiumBy.XPATH, WWS_SUBPROFILE_NAME_XPATH)
        wws_profile_0 = "Automation_test_abc,cockatoo image"
        wws_create_newProfile_btn = (AppiumBy.ACCESSIBILITY_ID, "Create a new profile")
        wws_edit_profiles_btn = (AppiumBy.ACCESSIBILITY_ID, "EDIT PROFILES")
        wws_view_policy_btn = (AppiumBy.ACCESSIBILITY_ID, "VIEW POLICY")
        wws_policy_text = (AppiumBy.ACCESSIBILITY_ID, POLICY_TEXT)
        wws_total_sub_profiles = (AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name,"image")]')

        # Create New Profile
        cnp_create_a_new_profile_title = (AppiumBy.ACCESSIBILITY_ID, "Create a new profile")
        cnp_your_name_label = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Your name"]')
        cnp_your_name_fld = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="Your name"]')
        cnp_child_profile_switch_label_btn = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@name="Is this a child profile?"]')
        cnp_alert_your_name_msg = (AppiumBy.ACCESSIBILITY_ID, "Please enter a profile name with at least ONE character")
        cnp_alert_your_name_red_icon = (AppiumBy.ACCESSIBILITY_ID, "error_filled/vector")
        cnp_next_btn = (AppiumBy.ACCESSIBILITY_ID, "NEXT")

        # Child Sub Profile
        cyb_child_year_of_birth_title = (AppiumBy.ACCESSIBILITY_ID, "Child’s year of birth")
        cyb_child_year_recommend_txt = (AppiumBy.ACCESSIBILITY_ID, 'Knowing your child’s age will help us recommend appropriate shows. Ie. 2020')
        cyb_child_year_fld = (AppiumBy.XPATH, '//XCUIElementTypeTextField[contains(@name,"year of birth")]')
        cyb_ios_done_key = (AppiumBy.ACCESSIBILITY_ID, "Done")
        cyb_ios_next_key = (AppiumBy.ACCESSIBILITY_ID, "Next:")
        cyb_ios_return_key = (AppiumBy.ACCESSIBILITY_ID, "Return")
        cyb_alert_to_enter_4_digit_year_of_birth_red_icon = (AppiumBy.ACCESSIBILITY_ID, "error_filled/vector")
        cyb_alert_to_enter_4_digit_year_of_birth_err = (AppiumBy.ACCESSIBILITY_ID, "Please enter a 4 digit year of birth Eg. 2016")


        # Shows we recommend
        swr_shows_we_recommend_title = (AppiumBy.ACCESSIBILITY_ID, "Shows we recommend")
        swr_shows_we_recommend_subtitle = (AppiumBy.ACCESSIBILITY_ID, "Please select at least one option to create a child’s profile")
        swr_abc_kids_switch = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[contains(@name,"ABC Kids, Shows for preschool children to explore")]')
        swr_abc_me_switch = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[contains(@name,"ABC ME, Shows to entertain school aged children")]')
        swr_alert_to_select_one_option_red_icon = (AppiumBy.ACCESSIBILITY_ID, "error_filled/vector")
        swr_alert_to_select_one_option_err = (AppiumBy.ACCESSIBILITY_ID, "Please select at least one option to create a child’s profile.")

        # Choose a Picture
        cap_choose_a_picture_title = (AppiumBy.ACCESSIBILITY_ID, "Choose a picture")
        CAP_PICTURE_NAME = "kookaburra" + " image"
        cap_picture_icon = (AppiumBy.XPATH, '//XCUIElementTypeCell[@name='f"{CAP_PICTURE_NAME}"']/XCUIElementTypeOther/XCUIElementTypeImage')
        cap_back_btn = (AppiumBy.ACCESSIBILITY_ID, "back")

        # Edit New Profile
        spe_select_profile_to_edit_title = (AppiumBy.ACCESSIBILITY_ID, "Select profile to edit")
        spe_done_btn = (AppiumBy.ACCESSIBILITY_ID, "DONE")

        # Edit Profile
        ep_edit_profile_title = (AppiumBy.ACCESSIBILITY_ID, "Edit Profile")
        ep_edit_picture_icon = (AppiumBy.ACCESSIBILITY_ID, CAP_PICTURE_NAME)
        ep_viewing_history_btn = (AppiumBy.ACCESSIBILITY_ID, "VIEWING HISTORY")
        ep_delete_profile_btn = (AppiumBy.ACCESSIBILITY_ID, "DELETE PROFILE")
        ep_for_help_txt = (AppiumBy.ACCESSIBILITY_ID, "For help")
        ep_iview_support_link = (AppiumBy.ACCESSIBILITY_ID, "IVIEW SUPPORT")

        # Edit Profile - Child
        epc_edit_child_profile_title = (AppiumBy.XPATH, "//*[contains(@name, 'Edit Child')]")
        epc_year_of_birth_label = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Year of birth"]')
        epc_year_of_birth_fld = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="Year of birth"]')

        # Viewing history
        vw_viewing_history_title = (AppiumBy.ACCESSIBILITY_ID, "Viewing history")
        vw_viewing_history_empty_txt = (AppiumBy.ACCESSIBILITY_ID, "Your viewing history is empty")
        vw_back_to_edit_profile_from_view_history_btn = (AppiumBy.ACCESSIBILITY_ID, "BACK TO EDIT PROFILE")
        vw_viewing_history_clear_btn = (AppiumBy.ACCESSIBILITY_ID, "CLEAR VIEWING HISTORY")
        vw_viewing_history_close_btn = (AppiumBy.ACCESSIBILITY_ID, "close")

        # Delete Profile
        dp_delete_profile_popup_title = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Delete profile"]')
        dp_delete_warning_txt = (AppiumBy.ACCESSIBILITY_ID, "Are you sure you want to delete RuntimeProfile profile from your account?")
        dp_cancel_btn = (AppiumBy.ACCESSIBILITY_ID, "Cancel")
        dp_delete_btn = (AppiumBy.ACCESSIBILITY_ID, "Delete")



        Edit_title_a11y = 'Select profile to edit'
        DONE_ACCESSIBILITY_ID = "DONE"
        FirstSubProfile_name = "Firstsubprofile"
        FirstSubProfile_btn = f"{FirstSubProfile_name},koala image"
        Child_profile_name = "NewKidProfile"
        Child_profile_btn = f"{Child_profile_name},frog image"
        Child_EditedProfile_name = "EditedProfileName"
        Child_editedProfile_btn = f"{Child_EditedProfile_name},frog image"

    elif ReadProperties.get_platform_name() == 'Android':

        # Who's watching screen
        wws_whos_watching_title = (AppiumBy.XPATH, '//*[contains(@text,"watching?")]')
        WWS_SUBPROFILE_NAME_XPATH = f'//*[@text="{SUBPROFILE_NAME}"]'
        wws_subprofile_btn = (AppiumBy.XPATH, WWS_SUBPROFILE_NAME_XPATH)
        wws_profile_0 = "Automation_test_abc,cockatoo image"
        wws_create_newProfile_btn = (AppiumBy.XPATH, "//*[@text='Create a new profile']")
        wws_edit_profiles_btn = (AppiumBy.XPATH, '//*[@text="EDIT PROFILES"]')
        wws_view_policy_btn = (AppiumBy.XPATH, '//*[@text="VIEW POLICY"]')
        wws_policy_text = (AppiumBy.XPATH, f'//*[@text="{POLICY_TEXT}"]')
        wws_total_sub_profiles = (AppiumBy.XPATH, '(//android.view.View[@index="0"])[position() > 1][not(@content-desc="Create profile")]')


        # Create New Profile
        cnp_create_a_new_profile_title = (AppiumBy.XPATH, "//*[@text='Create a new profile']")
        cnp_your_name_label = (AppiumBy.XPATH, '//*[@text="Your name"]')
        cnp_your_name_fld = (AppiumBy.XPATH, '//*[@text="Your name"]/following-sibling::android.widget.EditText[1]')
        cnp_child_profile_switch_label = (AppiumBy.XPATH, '//*[@text="Is this a child profile?"]')
        cnp_child_profile_switch_label_btn = (AppiumBy.ACCESSIBILITY_ID, 'switch')
        cnp_alert_your_name_msg = (AppiumBy.ACCESSIBILITY_ID, "Please enter a profile name with at least ONE character")
        cnp_alert_your_name_red_icon = (AppiumBy.ACCESSIBILITY_ID, "error_filled/vector")
        cnp_next_btn = (AppiumBy.XPATH, "//*[@text='NEXT']")

        # Child Sub Profile
        cyb_child_year_of_birth_title = (AppiumBy.XPATH, "//*[contains(@text,'s year of birth')]")
        cyb_child_year_recommend_txt = (AppiumBy.XPATH, "//*[contains(@text,'s age will help us recommend appropriate shows.')]")
        cyb_child_year_fld = (AppiumBy.XPATH, "//*[@text='Year of birth']/../..")
        cyb_ios_done_key = (AppiumBy.XPATH, "//*[@text='NEXT']")
        cyb_ios_next_key = (AppiumBy.XPATH, "//*[@text='NEXT']")
        cyb_ios_return_key = (AppiumBy.XPATH, "//*[@text='NEXT']")
        cyb_alert_to_enter_4_digit_year_of_birth_red_icon = (AppiumBy.XPATH, "//*[@content-desc='error']")
        cyb_alert_to_enter_4_digit_year_of_birth_err = (AppiumBy.XPATH, "//*[contains(@text, 's year of birth to continue')]")

        # Shows we recommend
        swr_shows_we_recommend_title = (AppiumBy.XPATH, "//*[@text='Shows we recommend']")
        swr_shows_we_recommend_subtitle = (AppiumBy.XPATH, "//*[contains(@text,'Please select at least one option to create a child')]")
        swr_abc_kids_switch = (AppiumBy.XPATH, '//*[contains(@text,"ABC Kids")]/..')
        swr_abc_me_switch = (AppiumBy.XPATH, '//*[contains(@text,"ABC ME")]/..')
        #swr_alert_to_select_one_option_red_icon = (AppiumBy.ACCESSIBILITY_ID, "error_filled/vector")
        #swr_alert_to_select_one_option_err = (AppiumBy.ACCESSIBILITY_ID, "Please select at least one option to create a child’s profile.")

        # Choose a Picture
        cap_choose_a_picture_title = (AppiumBy.XPATH, "//*[@text='Choose a picture']")
        CAP_PICTURE_NAME = "kookaburra"
        cap_picture_icon = (AppiumBy.XPATH, f'//android.widget.ImageView[@content-desc="{CAP_PICTURE_NAME}"]')
        cap_back_btn = (AppiumBy.ACCESSIBILITY_ID, "Back")

        # Edit New Profile
        spe_select_profile_to_edit_title = (AppiumBy.XPATH, "//*[@text='Select profile to edit']")
        spe_done_btn = (AppiumBy.XPATH, "//*[@text='DONE']")


        # Edit Profile
        ep_edit_profile_title = (AppiumBy.XPATH, "//*[@text='Edit Profile']")
        ep_edit_picture_icon = (AppiumBy.ACCESSIBILITY_ID, CAP_PICTURE_NAME+", select to change avatar image")
        ep_viewing_history_btn = (AppiumBy.XPATH, "//*[@text='VIEWING HISTORY']")
        ep_delete_profile_btn = (AppiumBy.XPATH, "//*[@text='DELETE PROFILE']")
        ep_for_help_txt = (AppiumBy.XPATH, "//*[@text='For help']")
        ep_iview_support_link = (AppiumBy.XPATH, "//*[@text='IVIEW SUPPORT']")

        # Edit Profile - Child
        epc_edit_child_profile_title = (AppiumBy.XPATH, "//*[contains(@text, 'Edit Child')]")
        epc_year_of_birth_label = (AppiumBy.XPATH, "//*[@text= 'Year of birth']")
        epc_year_of_birth_fld = (AppiumBy.XPATH, '//*[@text="Year of birth"]/following-sibling::android.widget.EditText[1]')

        # Viewing history
        vw_viewing_history_title = (AppiumBy.XPATH, "//*[@text= 'Viewing history']")
        vw_viewing_history_empty_txt = (AppiumBy.XPATH, "//*[@text= 'Your viewing history is empty']")
        vw_back_to_edit_profile_from_view_history_btn = (AppiumBy.XPATH, "//*[@text= 'BACK TO EDIT PROFILE']")
        vw_viewing_history_clear_btn = (AppiumBy.XPATH, "//*[@text= 'CLEAR VIEWING HISTORY']")
        vw_viewing_history_close_btn = (AppiumBy.XPATH, "//android.widget.Button")

        # Delete Profile
        dp_delete_profile_popup_title = (AppiumBy.XPATH, '//*[@text="Delete profile"]')
        dp_delete_warning_txt = (
        AppiumBy.ACCESSIBILITY_ID, '//*[contains(@text,"Are you sure you want to delete")]')
        dp_cancel_btn = (AppiumBy.XPATH, '//*[@text="CANCEL"]/following-sibling::android.widget.Button')
        dp_delete_btn = (AppiumBy.XPATH, '//*[@text="DELETE"]/following-sibling::android.widget.Button')

    else:
        pytest.fail("ERROR  - Check the Platform Name: " + str(ReadProperties.get_platform_name()))

    def __init__(self, app):
        super().__init__(app)

    def subprofile_btn_by_name(self, name: str):
        if ReadProperties.get_platform_name() == 'ios':
            sub_profile_ = ('xpath', f'//*[contains(@name, "{name}")]')
        elif ReadProperties.get_platform_name() == 'Android':
            sub_profile_ = ('xpath', f'//*[contains(@text, "{name}")]')#//*[contains(@content-desc,"kangaroo")]
        else:
            raise RuntimeError(f'Unsupported platform: {ReadProperties.get_platform_name()}')
        return sub_profile_

    def ep_subprofile_picture_btn_by_name(self, name: str):
        if ReadProperties.get_platform_name() == 'ios':
            sub_profile_ = ('xpath', f'//*[contains(@name, "{name}")]')
        elif ReadProperties.get_platform_name() == 'Android':
            sub_profile_ = ('xpath', f'//*[contains(@content-desc, "{name}")]')#//*[contains(@content-desc,"kangaroo")]
        else:
            raise RuntimeError(f'Unsupported platform: {ReadProperties.get_platform_name()}')
        return sub_profile_


    def picture_icon_by_image_name(self, name: str):
        if ReadProperties.get_platform_name() == 'ios':
            picture_icon = ('xpath', f'//XCUIElementTypeCell[@name="{name+" image"}"]/XCUIElementTypeOther/XCUIElementTypeImage')
        elif ReadProperties.get_platform_name() == 'Android':
            picture_icon = ('xpath', f'//android.widget.ImageView[@content-desc="{name}"]')#//*[contains(@content-desc,"kangaroo")]
        else:
            raise RuntimeError(f'Unsupported platform: {ReadProperties.get_platform_name()}')
        return picture_icon

    def spe_total_sub_profiles(self, index: int):
        spe_total_sub_profiles = (AppiumBy.XPATH, f'//android.view.View[@index="{index}"]')
        return spe_total_sub_profiles

    def clickOnMainProfileBtn(self):
        self.verifyTitleVisible()
        self.click(self.wws_subprofile_btn)

    def click_on_subprofile(self, subprofile):
        """
        Click on the desired profile by using profile locator
        :param subprofile: Must be in the same format as locators example iOS: profile_element ('accessibility id' , 'Profile_name')
        :return: None
        """
        self.verifyTitleVisible()
        self.click(subprofile)

    def verifyTitleVisible(self, timeout=None):

        if ReadProperties.get_platform_name() == 'Android':
            timeout = 10

        try:
            self.wait_implicit(2)
            self.wait_visible(self.wws_whos_watching_title, timeout=timeout)
        except Exception as e:
            self.logger.warning("Who's Watching Title does not exist. Continue to Login..." + str(e))
        return self.is_visible(self.wws_whos_watching_title)

    def return_or_hide_keyboard(self):
        if ReadProperties.get_platform_name() == 'ios':
            self.click(self.cyb_ios_return_key)
        else:
            self.hide_keyboard()

    def tap_switch_toggle_button(self, locator, status=False, percentage=1.0):
        if ReadProperties.get_platform_name() == 'ios':
            self.tap_toggle_switch_button(locator, status=status, percentage=percentage)
        elif ReadProperties.get_platform_name() == 'Android':
            self.tap(locator)

    def is_next_button_enabled(self):
        if ReadProperties.get_platform_name() == 'ios':
            self.is_enabled(self.cnp_next_btn)
        elif ReadProperties.get_platform_name() == 'Android':
            cnp_next_btn = (AppiumBy.XPATH, "//*[@text='NEXT']/..")
            self.is_enabled(cnp_next_btn)

    def navigate_to_whos_watching_screen(self, max_attempts: int):
        """
        Navigates back to the Whos Watching screen without creating a new subprofile.
        """
        for attempt in range(max_attempts):
            try:
                self.click(self.cap_back_btn)
                # Check if we have reached the Whos Watching screen
                if self.is_visible(self.wws_whos_watching_title):
                    self.logger.info("Navigated back to Whos watching Screen After clicking Back button : "+str(max_attempts)+" times")
                    return
            except ElementNotVisibleException:
                pass
        raise Exception("Could not navigate back to Whos Watching screen")
