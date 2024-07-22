import logging
import time

from selenium.common.exceptions import TimeoutException

from locators import instructor_locator
from locators.instructor_locator import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.admin_page import sessions_cover


class InstructorPage:
    def __init__(self, driver):
        self.driver = driver

    def start_session(self, locator):
        # Set the maximum number of refreshes you're willing to do
        max_refreshes = 10
        # Initialize a counter for the refreshes
        refresh_count = 0
        while refresh_count < max_refreshes:
            try:
                start_session_locator = (list(start_session.keys())[0], list(start_session.values())[0])
                start_session_element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(start_session_locator))
                start_session_element.click()
                break  # Exit the loop since the button is enabled and clicked
            except TimeoutException:
                # If the button is not enabled, refresh the page
                self.driver.refresh()
                refresh_count += 1

    def scheduled_session(self, locator):
        string_to_split = sessions_cover[0]
        # Split the string by comma
        list_workout = string_to_split.split(',')
        # If the "workout" is auto-selected.
        try:
            remove_workout_locator = (list(remove_workout.keys())[0], list(remove_workout.values())[0])
            remove_workout_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(remove_workout_locator))
            # remove_workout_element.click()
            time.sleep(2)
            self.select_topic_start_session(instructor_locator.session_scheduled)
        # If the "workout" is not auto-selected, it will select recommended sessions from a batch.
        except TimeoutException:
            # Today's Class Input Field
            class_locator = (list(today_class.keys())[0], list(today_class.values())[0])
            today_class_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(class_locator))
            today_class_element.click()
            # Iterating Each element of Workout
            for workout in list_workout:
                # logging.info("Instructor Page Portal Session covers: ", workout)
                today_class_element.send_keys(workout)
                today_class_element.send_keys(Keys.TAB)
                today_class_element.send_keys(Keys.ESCAPE)

            self.select_topic_start_session(instructor_locator.session_scheduled)

    def select_topic_start_session(self, locators):
        # Starting The Session
        choose_session_locator = (list(session_scheduled.keys())[0], list(session_scheduled.values())[0])
        choose_session_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(choose_session_locator))
        choose_session_element.click()

    def ins_take_attend(self, locators):
        # Take Attendance
        take_attend_locator = list(take_attend.keys())[0], list(take_attend.values())[0]
        take_attend_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(take_attend_locator))
        take_attend_element.click()

        # List of Tab storing in this variable
        list_windows = self.driver.window_handles
        # Iterating each Tab
        for window in list_windows:
            # switching Current Tab
            self.driver.switch_to.window(window)
            time.sleep(2)
            # Check if the title of the current Tab matches the expected title.
            if self.driver.title == "WizKlub - Student Attendance":
                logging.info("Title: %s", self.driver.title)
                # Select Attendance
                select_attend_locator = (list(select_attend.keys())[0], list(select_attend.values())[0])
                select_attend_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(select_attend_locator))
                select_attend_element.click()
                # saving Attendance btn
                save_attendance_locator = (list(save_attendance.keys())[0], list(save_attendance.values())[0])
                save_attendance_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(save_attendance_locator))
                save_attendance_element.click()
