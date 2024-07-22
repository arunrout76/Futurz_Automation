import logging
import time

from selenium.common.exceptions import TimeoutException
from Logs import log_config
from locators.user_locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.admin_page import sessions_cover

log = log_config.get_logs()


class StudentPage:
    def __init__(self, driver):
        self.driver = driver

    # Function for Click All Product in Side Navigation
    def all_product(self, locator):
        try:
            # X-path for all-product side navigation.
            all_product_locator = (list(all_products.keys())[0], list(all_products.values())[0])
            # Element storing in a variable.
            all_product_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(all_product_locator))
            # Click on that All Product Element
            all_product_element.click()
        except TimeoutException as e:
            log.error(f"Arun Error : {e}")

    def select_product(self, locators):
        try:
            # X-path specific Product
            product_locator = (list(product.keys())[0], list(product.values())[0])
            # specific Product Storing  in a variable
            product_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(product_locator))
            # click that Product
            product_element.click()
            # Xpath for Module
            module_locator = (list(module.keys())[0], list(module.values())[0])
            # Element of Module storing in a variable.
            module_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(module_locator))
            # Click that Element
            module_element.click()

        except TimeoutException as e:
            log.error(f"Arun Error:{e}")

    def all_workout(self, locator):
        string_to_batch = sessions_cover[0]
        batch_workout = string_to_batch.split(',')
        # string_to_batch = ["1-VisualAnalogies-Workout4"]
        # # Split the string by comma
        # batch_workout = string_to_batch[0].split(',')

        log.info(f"batch_workout{batch_workout}")

        try:
            # Looping List of Workout from batch
            for workouts in batch_workout:
                log.info(f"Arun: {workouts}")
                # Here the xpath for Workout Progress
                workout_progress_status_locator = ("xpath",
                                                   f"//a[@class='wiz-sessions-text text-wiz-ff6ba0' and text()='{workouts}']/../../div[3]/div[2]/div[1]/div")
                # Here element for Workout Progress
                workout_progress_status_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(workout_progress_status_locator))
                # Getting text of Progress Status.
                progress_status = workout_progress_status_element.text
                log.info(f"progress_status: {progress_status}")
                # Name of Workout Locator
                workout_name_locator = (
                "xpath", f"//a[@class='wiz-sessions-text text-wiz-ff6ba0' and text()='{workouts}']")
                # Name of Workout Element
                workout_name_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(workout_name_locator))
                # Condition for Workout Progress
                # if Progress is Completed
                if progress_status == "Completed":
                    # expected title of View Report page
                    expected_title = "WizKlub Playground - Visual Analogies"
                    try:
                        # if status completed then click on that Workout
                        workout_name_element.click()
                        # Getting Actual title of Completed Workout page.
                        actual_title = self.driver.title
                        # Here assertion.
                        assert actual_title == expected_title, f"title assertion with '{expected_title}' to '{actual_title}' "
                        # X-path for Navigating List of Session topic page
                        navigate_last_page_locator = (
                            list(navigate_last_page.keys())[0], list(navigate_last_page.values())[0])
                        # Navigating back page element storing in a variable
                        navigate_last_page_element = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located(navigate_last_page_locator))
                        # Click that Navigating back page Element
                        self.driver.execute_script("arguments[0].click();", navigate_last_page_element)
                    except Exception as e:
                        logging.error(f"this is an Exception{e}")

                # If Status of Work out is In-Progress.
                elif progress_status == "In Progress":
                    # click on that In-Progress Workout
                    workout_name_element.click()
                    self.attend_question(num_question)
                # If Work out Progress status is Un attended
                elif progress_status == "Unattended":
                    # click that Un-attended workout
                    workout_name_element.click()
                    # It's showing Popup for Initial if workout is in Un-attended state.
                    # X-path for popup
                    confirmation_popup_locator = (
                        list(confirmation_popup.keys())[0], list(confirmation_popup.values())[0])
                    # Element Storing in a Variable
                    confirmation_popup_element = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(confirmation_popup_locator))
                    # click on that Pop-up
                    confirmation_popup_element.click()

                    self.attend_question(num_question)
                    time.sleep(4)
                    self.verify_submit_popup(verify_submit)
                    time.sleep(4)
                    self.feedback_rating_popup(user_feedback)
                else:
                    pass
        except TimeoutException as e:
            log.error(f"This is Error {e}")

    def attend_question(self, locator):
        num_question_locator = (list(num_question.keys())[0], list(num_question.values())[0])
        num_question_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(num_question_locator))
        total_question = num_question_element.get_attribute("data-totalques")
        logging.info(f"Total Question{total_question}")
        number_questions = int(total_question)
        for i in range(1, number_questions+1):
            self.click_all_option(all_option)

            logging.info(f"Total Question{number_questions}")
            logging.info(f"Total Question: {type(number_questions)}")

    def click_all_option(self, locator):
        all_option_locator = (list(all_option.keys())[0], list(all_option.values())[0])
        all_option_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(all_option_locator))
        logging.info(f"all_option_element: {all_option_element}")
        logging.info(f"all_option_element: {len(all_option_element)}")
        for each_option in all_option_element:
            logging.info(f"options{each_option}")
            time.sleep(2)
            # Select One Option
            each_option.click()
            # Click on Next
            time.sleep(2)
            next_btn_locator = (list(next_question.keys())[0], list(next_question.values())[0])
            next_btn_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(next_btn_locator))
            last_level = next_btn_element.get_attribute("data-is_last_level")
            if last_level == "False":
                next_btn_element.click()
            else:
                submit_workout_locator = (list(submit_workout.keys())[0], list(submit_workout.values())[0])
                submit_workout_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(submit_workout_locator))
                # Click Submit Workout
                self.driver.execute_script("arguments[0].click();", submit_workout_element)
            time.sleep(2)
            # Hint Popup locator
            hint_popup_locator = (list(close_hint_popup.keys())[0], list(close_hint_popup.values())[0])
            # Storing Hint Popup element in a variable.
            hint_popup_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(hint_popup_locator))
            # if element is in Visibility.
            if hint_popup_element.is_displayed():
                logging.info(f"hint popup displaying: {hint_popup_element.is_displayed()}")
                time.sleep(2)
                hint_popup_element.click()
            else:
                break

    def verify_submit_popup(self, locator):
        verify_submit_locator = (list(verify_submit.keys())[0], list(verify_submit.values())[0])
        verify_submit_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(verify_submit_locator))
        verify_submit_element.click()

    def feedback_rating_popup(self, locator):
        user_feedback_locator = (list(user_feedback.keys())[0], list(user_feedback.values())[0])
        user_feedback_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(user_feedback_locator))
        user_feedback_element.send_keys("Thank you for providing such a valuable resource for kids")

        user_rating_locator = (list(user_rating.keys())[0], list(user_rating.values())[0])
        user_rating_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(user_rating_locator))
        # Choose a Rating
        self.driver.execute_script("arguments[0].click();", user_rating_element)
        #Submit Feedback Btn
        submit_feedback_locator = (list(submit_feedback.keys())[0], list(submit_feedback.values())[0])
        submit_feedback_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(submit_feedback_locator))
        submit_feedback_element.click()














    # def attend_assessment(self, locator):

    # Here store all the Workout to be Complete by Student
    # student_all_workouts = []
    # # Here locators for all Workouts for Student
    # workout_title_locator = (list(workout_title.keys())[0], list(workout_title.values())[0])
    # workout_title_element = WebDriverWait(self.driver, 10).until(
    #     EC.presence_of_all_elements_located(workout_title_locator))
    # # Iterating Each Workout of Student
    # for element in workout_title_element:
    #     # Get all Workout
    #     data_title = element.text
    #     # store in a List
    #     student_all_workouts.append(data_title)
    # log.info(f"Verify: {student_all_workouts}")
    # # Here iterating all the workout from batches
    # for plan_workout in batch_workout:
    #     # List comprehension
    #     # Find matching workouts between the planned workout from Batch and the student's all workout
    #     matching_workout = [workout for workout in student_all_workouts if plan_workout == workout]
    #     # Condition for matched Workout.
    #     if matching_workout:
    #         # Pass workout in Xpath and click according workout.
    #         workout_name_locator = ("xpath", f"//a[@class='wiz-sessions-text text-wiz-ff6ba0' and text()='{matching_workout[0]}']")
    #         workout_name_element = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located(workout_name_locator))
    #         workout_name_element.click()
    #         log.info(f"planned workout{plan_workout} : {matching_workout}")
    #     else:
    #         log.info(f"not planned workout {plan_workout}")
