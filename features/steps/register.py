from behave import *
from features.pages.HomePage import HomePage
from features.steps.Utility import EmailWithTimeStampGenerator
from features.steps.Utility.RandomStringGeneration import random_number_generator, random_string_generator


@given('I navigate to Register Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()


@when('I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        new_email = EmailWithTimeStampGenerator.get_new_mail_with_timestamp()
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone_value(random_number_generator())
        random_value = random_string_generator()
        context.register_page.enter_password(random_value)
        context.register_page.enter_confirm_password_value(random_value)


@when('I select Privacy Policy option')
def step_impl(context):
    context.register_page.click_on_privacy_policy()


@when('I click on Continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_on_continue_button()


@then('Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.account_success_page.successful_account_creation(expected_text)


@when('I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        new_email = EmailWithTimeStampGenerator.get_new_mail_with_timestamp()
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone_value(random_number_generator())
        random_value = random_string_generator()
        context.register_page.enter_password(random_value)
        context.register_page.enter_confirm_password_value(random_value)
        context.register_page.subscribe_news_letter_option()


@when('I enter below details into all fields except email field')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone_value(random_number_generator())
        random_value = random_string_generator()
        context.register_page.enter_password(random_value)
        context.register_page.enter_confirm_password_value(random_value)
        context.register_page.subscribe_news_letter_option()


@when('I enter existing accounts email into email field')
def step_impl(context):
    context.register_page.enter_email("chandra1234@gmail.com")


@then('Proper warning message information about duplicate account should be displayed')
def step_impl(context):
    expected_warning_message = "Warning: E-Mail Address is already registered!"
    assert context.register_page.email_already_exist_message(expected_warning_message)


@when('I dont enter anything into the fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone_value("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm_password_value("")
    context.register_page.subscribe_news_letter_option()


@then('Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    context.expected_privacy_policy = "Warning: You must agree to the Privacy Policy!"
    context.expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    context.expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    context.expected_email_warning = "E-Mail Address does not appear to be valid!"
    context.expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    context.expected_password_warning = "Password must be between 4 and 20 characters!"
    assert context.register_page.display_status_of_all_warning_message(context.expected_privacy_policy,
                                                                       context.expected_first_name_warning,
                                                                       context.expected_last_name_warning,
                                                                       context.expected_email_warning,
                                                                       context.expected_telephone_warning,
                                                                       context.expected_password_warning)
