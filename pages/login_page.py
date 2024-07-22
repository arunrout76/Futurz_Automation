from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logs import log_config
from Utility.error_detector import Detector
from locators.login_locators import *

log = log_config.get_logs()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_page(self, locators):
        self.driver.find_element(list(login_btn.keys())[0], list(login_btn.values())[0]).click()

    def credential(self, locators, username):
        self.driver.find_element(list(input_username.keys())[0], list(input_username.values())[0]).send_keys(username)

    def next_button(self, locators):
        self.driver.find_element(list(next_btn.keys())[0], list(next_btn.values())[0]).click()

    def pwd_credential(self, locators, pwd):
        flag = False
        try:
            self.driver.find_element(list(input_pwd.keys())[0], list(input_pwd.values())[0]).send_keys(pwd)
            flag = True
        except Exception as e:
            log.error(f"Password Locator not Found {e}")
        return flag

    def verify_password(self, locators):
        flag = False
        try:
            verify_btn_locator = (list(verify_btn.keys())[0], list(verify_btn.values())[0])
            verify_btn_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(verify_btn_locator))
            verify_btn_element.click()
            flag = True
        except Exception as e:
            log.error(f"Verify and Proceed x-path not correct {e}")
        return flag

    def correct_credential_popup(self, locators):
        flag = False
        try:
            expected_popup = "You have successfully logged in"
            popup_locator = (list(popup_message.keys())[0], list(popup_message.values())[0])
            actual_popup = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(popup_locator)).text
            assert actual_popup == expected_popup
            log.info(f"Pop-up displayed: {actual_popup}")
            flag = True
        except Exception as e:
            log.error(f"Verify x-path of popup {e}")
        return flag

    def incorrect_credential_popup(self, locators):
        flag = False
        try:
            expected_popup = "Please enter correct password to login!"
            popup_locator = (list(popup_message.keys())[0], list(popup_message.values())[0])
            actual_popup = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(popup_locator)).text
            assert actual_popup == expected_popup
            log.info(f"Pop-up displayed: {actual_popup}")
            flag = True
        except Exception as e:
            log.error(f"Verify x-path of popup {e}")
        return flag

    def without_pwd_popup(self, locators):
        flag = False
        try:
            expected_popup = "Missing required parameter PASSWORD"
            popup_locator = (list(popup_message.keys())[0], list(popup_message.values())[0])
            actual_popup_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(popup_locator))
            actual_popup_text = actual_popup_element.text
            assert actual_popup_text == expected_popup
            log.info(f"Pop-up displayed: {actual_popup_text}")
            flag = True
        except Exception as e:

            # error_spot = Detector(self.driver)
            # error_spot.detect_error(actual_popup_element)

            log.error(f"Verify x-path of popup {e}")
        return flag



