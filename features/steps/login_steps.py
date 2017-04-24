from behave import given, when, then, use_step_matcher
from hamcrest import assert_that, equal_to
import re
from login_utils import *
import time

@given(u'a user visits the login page')
@when(u'a user visits the login page')
def visit_login(ctx):
    ctx.browser.get(ctx.home+"/login")


@then(u'she should see the username field')
def see_username_field(ctx):
    username_field_found = re.search("username", ctx.browser.page_source, re.IGNORECASE)
    assert username_field_found


@then(u'she should see the password field')
def see_password_field(ctx):
    password_field_found = re.search("password", ctx.browser.page_source, re.IGNORECASE)
    assert password_field_found


@then(u'she should see the login button')
def see_login_button(ctx):
    login_btn_found = re.search("login", ctx.browser.page_source, re.IGNORECASE)
    #login_btn = driver.find_element_by_name('login')
    #assert login_btn
    assert login_btn_found


@when(u'she logs in with username "{username}" and password "{password}"')
def login(ctx, username, password):
    driver = ctx.browser
    driver.get(ctx.home + "/login")
    uname = driver.find_element_by_name('username')
    passwd = driver.find_element_by_name('password')
    login_button = driver.find_element_by_id('btn_login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()
    time.sleep(1)


@then(u'she should see a message of login success')
def see_login_success(ctx):
    login_success_found = re.search("login success", ctx.browser.page_source, re.IGNORECASE)
    assert login_success_found


@then(u'she should see a message of login failure')
def see_login_failure(ctx):
    login_failure_found = re.search("Bad Login", ctx.browser.page_source, re.IGNORECASE)
    assert login_failure_found


@given(u'she sees the Logout link')
def see_logout_link(ctx):
    login(ctx,"admin","admin")
    logout_link_found = re.search("log out", ctx.browser.page_source, re.IGNORECASE)
    assert logout_link_found


@when(u'she logs out')
def logging_out(ctx):
    driver = ctx.browser
    ctx.browser.get(ctx.home + "/logout")

@then(u'she sees a message telling her she has logged out')
def see_logout_success(ctx):
    logout_msg_found = re.search("logged out", ctx.browser.page_source, re.IGNORECASE)
    assert logout_msg_found