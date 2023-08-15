from typing import Tuple

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from page_objects.abc_iview_tv.base_ui import BaseUI
from utilities.read_properties import ReadProperties


class LinkTvScreen(BaseUI):
    if ReadProperties.get_platform_name() == 'tvOS':
        tv_link_tv_scan_qr_1_website_title = (AppiumBy.XPATH, "//*[@name= '1, Scan the QR code OR visit the website:, "
                                                              "abc.net.au/linktv']")
        tv_link_tv_follow_instructions_2_title = (AppiumBy.XPATH, '//*[normalize-space(@name)="2, Follow the instructions to log in or sign up for an ABC account."]')
        tv_link_tv_unique_code_ele = (AppiumBy.XPATH, "//*[starts-with(@name, '3, Enter your unique code:')]")

    elif ReadProperties.get_platform_name() == 'Android':
        tv_link_tv_unique_code_ele = (AppiumBy.XPATH, "//*[@index= '8']")

    elif ReadProperties.get_platform_name() == 'web':
        pass

    else:
        pytest.fail("ERROR - Check the Platform Name: " + str(ReadProperties.get_platform_name()))

    def __init__(self, app):
        super().__init__(app)

    def extract_unique_code(self):
        self.utils.wait_visible(self.tv_link_tv_unique_code_ele, timeout=5)
        full_text = self.get_attribute(self.tv_link_tv_unique_code_ele,
                                       "value" if ReadProperties.get_platform_name() == 'tvOS' else "text")

        if ReadProperties.get_platform_name() == 'tvOS':
            parts = full_text.split(',')
            unique_code_parts = [part.strip() for part in parts if part.strip().isalpha()]
            unique_code = ''.join(unique_code_parts)
        else:  # For Android
            unique_code = full_text.replace(" ", "")

        # Check conditions using the functions
        is_alphabetic = unique_code.isalpha()
        is_4_digits = len(unique_code) == 4 and unique_code.isdigit()
        has_no_numeric = not any(char.isdigit() for char in unique_code)

        return unique_code, is_alphabetic, is_4_digits, has_no_numeric

    def login_api(self, ctv_login_url: str, api_key: str, user_email: str, password: str) -> Tuple[str, str, str, str]:
        self.api_utils.set_body({
            "apiKey": api_key,
            "loginID": user_email,
            "password": password,
            "include": "id_token"
        })
        response_json = self.api_utils.post_request(ctv_login_url)

        if response_json.get("statusCode") == 200:
            uid = response_json.get("UID")
            uid_signature = response_json.get("UIDSignature")
            signature_timestamp = response_json.get("signatureTimestamp")
            id_token = response_json.get("id_token")
            return uid, uid_signature, signature_timestamp, id_token

        else:
            error_message = response_json.get("errorMessage")
            error_details = response_json.get("errorDetails")
            raise Exception(f"Login link tv API returned an error: {error_message} , Error Details: {error_details}")

    def verify_api(self, ctv_verify_url: str, api_key: str, id_token: str, uid: str,
                   uid_signature: str, signature_timestamp: str, code: str) -> Tuple[int, str, str]:
        headers = {
            "Authorization": f"Bearer {id_token}",
            "x-api-key": api_key
        }
        self.api_utils.set_headers(headers)
        self.api_utils.set_body({
            "UID": uid,
            "UIDSignature": uid_signature,
            "signatureTimestamp": signature_timestamp,
            "code": code
        })
        response_json = self.api_utils.post_request(ctv_verify_url, use_json=True)

        if "statusCode" in response_json:
            status_code = response_json.get("statusCode")
            if status_code == 200:
                request_id = response_json.get("requestId")
                time = response_json.get("time")
                return status_code, request_id, time
            else:
                error_message = response_json.get("error")
                raise Exception(f"Status: {status_code} , Error: {error_message} ")
        else:
            # Handle the error response
            error_message = response_json.get("error")
            raise Exception("Verify link tv API returned an error: " + error_message)

    def link_tv_with_abc_account(self, ctv_login_url: str, ctv_verify_url: str, api_key: str,
                                 user_email: str, password: str) -> bool:
        code = '1234'
        self.logger.info("Unique code from tv screen: " + str(code))

        # LOGIN API request
        uid, uid_signature, signature_timestamp, id_token = self.login_api(ctv_login_url, api_key, user_email, password)

        try:
            # VERIFY API request
            status_code, request_id, time = self.verify_api(ctv_verify_url, api_key, id_token, uid, uid_signature,
                                                            signature_timestamp, code)
            self.logger.info("Response statusCode: " + str(status_code))
            self.logger.info("Response requestId: " + str(request_id))
            self.logger.info("Response time: " + str(time))

            if status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            self.logger.error("Error occurred: " + str(e))
            raise
