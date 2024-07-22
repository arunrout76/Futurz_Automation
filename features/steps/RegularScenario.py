import time

from behave import *
from Logs import log_config
from pages.login_page import LoginPage
from pages.admin_page import AdminPage, sessions_cover
from pages.instructor_page import InstructorPage
from pages.student_page import StudentPage
from locators import login_locators, admin_locators, instructor_locator, user_locators

log = log_config.get_logs()


# ------------------------------Click on Login with correct Login and Password.------------------------------
@given('Reschedule the Batch from Username as "{uname}" and Password as "{pwd}" and batch is "{batch}"')
def admin_cred(context, uname, pwd, batch):
    status = False
    try:
        login = LoginPage(context.driver)
        admin = AdminPage(context.driver)
        login.login_page(login_locators.login_btn)
        login.credential(login_locators.input_username, uname)
        login.next_button(login_locators.next_btn)
        login.pwd_credential(login_locators.input_pwd, pwd)
        login.verify_password(login_locators.verify_btn)
        admin.three_dot(admin_locators.header_three_dot)
        admin.manage_analytics(admin_locators.management_analytics)
        admin.all_batches(admin_locators.nav_batch)
        admin.b2b_card(admin_locators.b2b)
        admin.all_card(admin_locators.all_category)
        admin.processing(admin_locators.data_table_loader)
        admin.search(admin_locators.search_field, batch)
        admin.search_click(admin_locators.search_btn)
        admin.processing(admin_locators.data_table_loader)
        admin.view_batch(admin_locators.batch_view)
        admin.session_tab(admin_locators.session_progress)
        admin.reschedule(admin_locators.list_row)

        status = True
    except Exception as e:
        log.error(f"Exception Occurred: {e}")
    assert status is True, "configured wrong X-PATH. "


@when('The batch has been rescheduled for Now')
def reschedule(context):
    admin = AdminPage(context.driver)
    admin.confirm_reschedule(admin_locators.confirm_reschedule_btn)
    ss_cvr = ''.join(sessions_cover)
    print("This is session : " + ss_cvr)
    log.info(ss_cvr)
    # assert status is True, "verify the x-path"


@then('Rescheduled Successfully')
def reschedule_successful(context):
    admin = AdminPage(context.driver)
    status = admin.confirm_popup(admin_locators.popup_message)
    assert status is True, "Check Screenshot"


@given('Reschedule the Batch from Instructor Username as "{uname}" and Password as "{pwd}"')
def instructor_login(context, uname, pwd):
    login = LoginPage(context.driver)
    ins = InstructorPage(context.driver)
    login.login_page(login_locators.login_btn)
    login.credential(login_locators.input_username, uname)
    login.next_button(login_locators.next_btn)
    login.pwd_credential(login_locators.input_pwd, pwd)
    login.verify_password(login_locators.verify_btn)
    ins.start_session(instructor_locator.start_session)


@when('Start the Session')
def session_schedule(context):
    ins = InstructorPage(context.driver)
    ins.scheduled_session(instructor_locator.today_class)
    ins = InstructorPage(context.driver)
    ins.ins_take_attend(instructor_locator.take_attend)


@then('Take Attendance')
def take_attendance(context):
    pass


@given('Reschedule the Batch from Student Username as "{uname}" and Password as "{pwd}"')
def user_login(context, uname, pwd):
    login = LoginPage(context.driver)
    login.login_page(login_locators.login_btn)
    login.credential(login_locators.input_username, uname)
    login.next_button(login_locators.next_btn)
    login.pwd_credential(login_locators.input_pwd, pwd)
    login.verify_password(login_locators.verify_btn)


@when('Workouts are Completed')
def attend_workout(context):
    student = StudentPage(context.driver)
    student.all_product(user_locators.all_products)
    student.select_product(user_locators.product)
    student.all_workout(user_locators.workout_title)


@then('Feedback is Given')
def feedback_rate(context):
    pass
