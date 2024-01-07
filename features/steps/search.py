from behave import *
from features.pages.HomePage import HomePage


@given('Navigated to Home Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    expected_title = "Your Store"
    assert context.home_page.verify_home_page_title(expected_title)


@when('Enter valid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box(product)


@when('Click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()


@then('valid product should get displayed in Search results')
def step_impl(context):
    assert context.search_page.display_valid_product_search()


@when('Enter invalid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box(product)


@when('dont enter anything into Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box("")


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria.abc"
    assert context.search_page.display_message_search_results(expected_text)
