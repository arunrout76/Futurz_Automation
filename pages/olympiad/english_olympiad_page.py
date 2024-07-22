import logging
import time

from locators.english_olympiad_locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AllOlympiad:
    def __init__(self, driver):
        self.driver = driver

    def participate_now(self, locator):
        participate_now_locator = (list(participate_now.keys())[0], list(participate_now.values())[0])
        participate_now_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(participate_now_locator))
        participate_now_element.click()

    def choose_option(self, locator):
        total_que_locator = (list(total_que.keys())[0], list(total_que.values())[0])
        total_que_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(total_que_locator))
        raw_num_questions = total_que_element.get_attribute("data-totalques")
        num_questions = int(raw_num_questions)
        logging.info(f"total question:{num_questions}")

        for question_item in range(1, num_questions):
            logging.info(f"question_item")
            time.sleep(2)
            option_locator = (list(option.keys())[0], list(option.values())[0])
            option_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(option_locator))
            option_element.click()
            time.sleep(2)
            next_que_locator = (list(next_que.keys())[0], list(next_que.values())[0])
            next_que_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(next_que_locator))
            next_que_element.click()

        time.sleep(2)
        option_locator = (list(option.keys())[0], list(option.values())[0])
        option_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(option_locator))
        option_element.click()
        time.sleep(2)
        submit_test_locator = (list(submit_test.keys())[0], list(submit_test.values())[0])
        submit_test_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submit_test_locator))
        submit_test_element.click()

    def submit_popup(self, locator):
        submit_popup_locator = (list(final_submit.keys())[0], list(final_submit.values())[0])
        submit_popup_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submit_popup_locator))
        submit_popup_element.click()

        time.sleep(10)
        student_name_locator = (list(home_page.keys())[0], list(home_page.values())[0])
        student_name_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(student_name_locator))

        self.driver.execute_script("arguments[0].click();", student_name_element)

        # student_name_element.click()
        # std = len(student_name_element)
        # logging.info(f"name of student:{std}")
