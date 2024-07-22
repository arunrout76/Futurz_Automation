import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logs import log_config
from Utility.error_detector import Detector
from pages import login_page
from locators.admin_locators import *
import datetime
from datetime import timedelta

log = log_config.get_logs()

sessions_cover = []


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def three_dot(self, locators):
        header_locator = (list(header_three_dot.keys())[0], list(header_three_dot.values())[0])
        header = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(header_locator))
        header.click()

    def manage_analytics(self, manage):
        manage_locator = (list(management_analytics.keys())[0], list(management_analytics.values())[0])
        manage = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(manage_locator))
        manage.click()

    def all_batches(self, batch):
        nav_batch_locator = list(nav_batch.keys())[0], list(nav_batch.values())[0]
        batches = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(nav_batch_locator))
        batches.click()

    def b2b_card(self, locators):
        b2b_locator = (list(b2b.keys())[0], list(b2b.values())[0])
        b2b_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(b2b_locator))
        b2b_element.click()

    def all_card(self, locators):
        all_locator = (list(all_category.keys())[0], list(all_category.values())[0])
        all_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(all_locator))
        all_element.click()

    def processing(self, locators):
        loader_locator = (list(data_table_loader.keys())[0], list(data_table_loader.values())[0])
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loader_locator))

    def search(self, locators, batch):
        search_locator = (list(search_field.keys())[0], list(search_field.values())[0])
        search_element = (WebDriverWait(self.driver, 10)
                          .until(EC.presence_of_element_located(search_locator)))
        search_element.send_keys(batch)

    def search_click(self, locators):
        search_btn_locator = (list(search_btn.keys())[0], list(search_btn.values())[0])
        search_btn_element = (WebDriverWait(self.driver, 10)
                              .until(EC.presence_of_element_located(search_btn_locator)))
        search_btn_element.click()

    def view_batch(self, locators):
        view_locator = (list(batch_view.keys())[0], list(batch_view.values())[0])
        view_element = (WebDriverWait(self.driver, 10)
                        .until(EC.presence_of_element_located(view_locator)))
        view_element.click()
        return view_element

    def session_tab(self, locators):
        session_locator = (list(session_progress.keys())[0], list(session_progress.values())[0])
        session_progress_element = (WebDriverWait(self.driver, 10)
                                    .until(EC.presence_of_element_located(session_locator)))
        session_progress_element.click()

    def reschedule(self, locators):
        today = datetime.date.today()
        format_date = today.strftime("%m%d%Y")
        current_time = datetime.datetime.now()
        # advance_time = current_time + timedelta(minutes=1)
        advance_time = current_time + timedelta(hours=5, minutes=31)
        set_time = advance_time.strftime("%I:%M%p")
        table_locator = (list(list_row.keys())[0], list(list_row.values())[0])

        batch_status_element = (WebDriverWait(self.driver, 10)
                                .until(EC.presence_of_all_elements_located(table_locator)))
        for data_rows in batch_status_element:
            find_text = "Scheduled"
            if find_text in data_rows.text:
                reschedule_locator = (list(reschedule_btn.keys())[0], list(reschedule_btn.values())[0])
                session_covered_locator = (list(session_covered.keys())[0], list(session_covered.values())[0])

                reschedule_element = (WebDriverWait(self.driver, 10)
                                      .until(EC.presence_of_element_located(reschedule_locator)))

                session_covered_element = (WebDriverWait(self.driver, 10)
                                           .until(EC.presence_of_element_located(session_covered_locator)))
                sessions_cover.append(session_covered_element.text)
                log.info(f"data Rendering from Batch{session_covered_element.text}")
                reschedule_element.click()
                time.sleep(5)
                reschedule_date_locator = (list(reschedule_date.keys())[0], list(reschedule_date.values())[0])
                reschedule_date_element = (WebDriverWait(self.driver, 10)
                                           .until(EC.presence_of_element_located(reschedule_date_locator)))
                reschedule_date_element.send_keys(format_date)
                reschedule_date_element.send_keys(Keys.TAB)
                reschedule_date_element.send_keys(set_time)

                reschedule_cls_drn_locator = (list(reschedule_cls_drn.keys())[0], list(reschedule_cls_drn.values())[0])
                reschedule_cls_drn_element = (WebDriverWait(self.driver, 10)
                                              .until(EC.presence_of_element_located(reschedule_cls_drn_locator)))
                reschedule_cls_drn_element.clear()
                reschedule_cls_drn_element.send_keys("2")

                reschedule_cat_locator = list(reschedule_cat.keys())[0], list(reschedule_cat.values())[0]
                reschedule_cat_element = (WebDriverWait(self.driver, 10)
                                          .until(EC.presence_of_element_located(reschedule_cat_locator)))
                reschedule_cat_element.click()

                reschedule_drpdwn_locator = (
                    list(reschedule_cat_drpdwn.keys())[0], list(reschedule_cat_drpdwn.values())[0])
                reschedule_drpdwn_element = (WebDriverWait(self.driver, 10)
                                             .until(EC.presence_of_element_located(reschedule_drpdwn_locator)))
                reschedule_drpdwn_element.click()

                reschedule_reason_locator = list(reschedule_reason.keys())[0], list(reschedule_reason.values())[0]
                reschedule_reason_element = (WebDriverWait(self.driver, 10)
                                             .until(EC.presence_of_element_located(reschedule_reason_locator)))
                reschedule_reason_element.send_keys("Arun")
                break

    def confirm_reschedule(self, locators):
        flag = False
        try:
            confirm_reschedule_locator = (
                list(confirm_reschedule_btn.keys())[0], list(confirm_reschedule_btn.values())[0])
            confirm_reschedule_element = (WebDriverWait(self.driver, 10)
                                          .until(EC.presence_of_element_located(confirm_reschedule_locator)))
            confirm_reschedule_element.click()
            flag = True
        except TimeoutException as e:
            error_spot = Detector(self.driver)
            error_spot.detect_error(confirm_reschedule_element)
        return flag

    def confirm_popup(self, locator):
        flag = False
        expected_popup = "Success"
        try:
            popup_locator = (list(popup_message.keys())[0], list(popup_message.values())[0])
            actual_popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(popup_locator)).text
            assert expected_popup == actual_popup
            log.info(f"Pop-up displayed: {actual_popup}")
            flag = True
        except TimeoutException as e:
            # error_spot = Detector(self.driver)
            # error_spot.detect_error(actual_popup)
            log.info(f"Pop-up displayed: {actual_popup}")
        return flag
