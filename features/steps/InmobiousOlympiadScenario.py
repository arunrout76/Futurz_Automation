import logging

from behave import *
from Logs import log_config
from pages.olympiad.english_olympiad_page import AllOlympiad
from locators import english_olympiad_locators

log = log_config.get_logs()


@given("Attend Assessment")
def participate_now(context):
    status = False
    try:
        ap = AllOlympiad(context.driver)
        ap.participate_now(english_olympiad_locators.participate_now)
        ap.choose_option(english_olympiad_locators.option)
        status = True
    except Exception as e:
        logging.error(f"exception Occurred {e}")
    assert status is True


@when("Submit Assessment")
def submit_assessment(context):
    status = False
    try:
        sp = AllOlympiad(context.driver)
        sp.submit_popup(english_olympiad_locators.final_submit)
        status = True
    except Exception as e:
        logging.error(f"Exception Occurred {e}")
    assert status is True


@then("Generate Report")
def view_report(context):
    pass
