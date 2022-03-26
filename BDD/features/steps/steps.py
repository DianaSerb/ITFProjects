from behave import *


@given(u'I have Behave installed')
def step_impl(context):
    print("Step 1")


@when(u'I execute a test')
def step_impl(context):
    print("Step 2")


@then(u'Results should be provided')
def step_impl(context):
    print("Step 3")
