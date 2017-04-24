from behave import given, when, then, use_step_matcher
from hamcrest import assert_that, equal_to
import re
import time
from login_utils import *

@given(u'a user visits the site')
def visit(ctx):
    ctx.browser.get(ctx.home)


@then(u'she should see CoinMart')
def see(ctx):
    coinmart_found = re.search("CoinMart", ctx.browser.page_source, re.IGNORECASE)
    assert coinmart_found


@given(u'she is not logged in')
def is_not_logged_in(ctx):
    # can't really test this except if one sees the Login link
    pass

@then(u'she should see the Login link')
def see_login(ctx):
    login_found = re.search("log in", ctx.browser.page_source, re.IGNORECASE)
    assert login_found


@when(u'she logs in')
def logs_in(ctx):
    driver = ctx.browser
    driver.get(ctx.home + "/login")
    uname = driver.find_element_by_name('username')
    passwd = driver.find_element_by_name('password')
    login_button = driver.find_element_by_id('btn_login')
    uname.clear();
    passwd.clear();
    uname.send_keys('admin')
    passwd.send_keys('admin')
    login_button.click()
    time.sleep(2)
    logged_in_found = re.search("login success", ctx.browser.page_source, re.IGNORECASE)
    assert logged_in_found

@when(u'she returns to the site')
def return_visit(ctx):
    ctx.browser.get(ctx.home)


@then(u'she should see the Logout link')
def step_impl(ctx):
    logout_found = re.search("log out", ctx.browser.page_source, re.IGNORECASE)
    assert logout_found
