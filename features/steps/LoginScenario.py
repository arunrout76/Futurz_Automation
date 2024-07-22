from behave import *
from Logs import log_config
from pages.login_page import LoginPage
from locators import login_locators

log = log_config.get_logs()


# ------------------------------Click on Login with correct Login and Password.------------------------------
@given('Username is "{uname}" and Password is "{pwd}"')
def cred_give(context, uname, pwd):
    status = False
    try:
        login = LoginPage(context.driver)
        login.login_page(login_locators.login_btn)
        login.credential(login_locators.input_username, uname)
        login.next_button(login_locators.next_btn)
        login.pwd_credential(login_locators.input_pwd, pwd)
        status = True
    except Exception as e:
        log.error(f"Exception Occurred: {e}")
    assert status is True, "configured wrong X-PATH either user name or Password "


@when('Correct Credential')
def login_btn(context):
    login = LoginPage(context.driver)
    status = login.verify_password(login_locators.verify_btn)
    assert status is True, "verify the x-path"


@then('Login Successful')
def popup_msg(context):
    login = LoginPage(context.driver)
    status = login.correct_credential_popup(login_locators.popup_message)
    assert status is True, "Check xpath"


# --------------------------------------------Click on Login with Wrong Password.----------------------
@given('Username is "{uname}" and Wrong Password is "{pwd}"')
def cred_give(context, uname, pwd):
    status = False
    try:
        login = LoginPage(context.driver)
        login.login_page(login_locators.login_btn)
        login.credential(login_locators.input_username, uname)
        login.next_button(login_locators.next_btn)
        login.pwd_credential(login_locators.input_pwd, pwd)
        status = True
    except Exception as e:
        log.error(f"Exception Occurred: {e}")
    assert status is True, "configured wrong X-PATH either user name or Password "


@when('In-Correct Credential')
def login_btn(context):
    login = LoginPage(context.driver)
    status = login.verify_password(login_locators.verify_btn)
    assert status is True, "verify the x-path"


@then('Login Failed')
def popup_msg(context):
    login = LoginPage(context.driver)
    status = login.incorrect_credential_popup(login_locators.popup_message)
    assert status is True, "Check xpath"


# --------------------------------------------Click on Login without Inserting Password.----------------------
@given('Username is "{uname}" and Wrong Password as Empty field')
def cred_give(context, uname):
    status = False
    try:
        login = LoginPage(context.driver)
        login.login_page(login_locators.login_btn)
        login.credential(login_locators.input_username, uname)
        login.next_button(login_locators.next_btn)
        status = True
    except Exception as e:
        log.error(f"Exception Occurred: {e}")
    assert status is True, "configured wrong X-PATH either user name or Password "


@when('No Password')
def login_btn(context):
    login = LoginPage(context.driver)
    status = login.verify_password(login_locators.verify_btn)
    assert status is True, "verify the x-path"


@then('Error popup while Login Failed')
def popup_msg(context):
    login = LoginPage(context.driver)
    status = login.without_pwd_popup(login_locators.popup_message)
    assert status is True, "Check xpath"






