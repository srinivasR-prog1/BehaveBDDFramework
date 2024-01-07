from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_name = "firstname"
    last_name_field_name = "lastname"
    email_field_name = "email"
    telephone_field_name = "telephone"
    password_field_name = "password"
    password_confirm_field_name = "confirm"
    privacy_policy_option_name = "agree"
    continue_button_xpath = "//input[@type='submit']"
    news_letter_subscribe_xpath = "//input[@name='newsletter'][@value='1']"
    warning_message_email_exist_xpath = "//div[@id='account-register']/div[1]"
    warning_message_privacy_policy_xpath = "//div[@class = 'alert alert-danger alert-dismissible']"
    warning_first_name_xpath = "//input[@id='input-firstname']/following-sibling::div"
    warning_last_name_xpath = "//input[@id='input-lastname']/following-sibling::div"
    warning_email_xpath = "//input[@id='input-email']/following-sibling::div"
    warning_telephone_xpath = "//input[@id='input-telephone']/following-sibling::div"
    warning_password_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.enter_into_element("first_name_field_name", self.first_name_field_name, first_name_text)

    def enter_last_name(self, last_name_text):
        self.enter_into_element("last_name_field_name", self.last_name_field_name, last_name_text)

    def enter_email(self, email_text):
        self.enter_into_element("email_field_name", self.email_field_name, email_text)

    def enter_telephone_value(self, telephone_number):
        self.enter_into_element("telephone_field_name", self.telephone_field_name, telephone_number)

    def enter_password(self, password_value):
        self.enter_into_element("password_field_name", self.password_field_name, password_value)

    def enter_confirm_password_value(self, confirm_password_value):
        self.enter_into_element("password_confirm_field_name", self.password_confirm_field_name, confirm_password_value)

    def click_on_privacy_policy(self):
        self.click_on_element("privacy_policy_option_name", self.privacy_policy_option_name)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def subscribe_news_letter_option(self):
        self.click_on_element("news_letter_subscribe_xpath", self.news_letter_subscribe_xpath)

    def email_already_exist_message(self, expected_warning_message):
        return self.retrieve_element_text_contains("warning_message_email_exist_xpath",
                                                   self.warning_message_email_exist_xpath, expected_warning_message)

    def display_status_of_all_warning_message(self, expected_privacy_policy_message, expected_first_name_warning,
                                              expected_last_name_warning, expected_email_warning,
                                              expected_telephone_warning, expected_password_xpath):
        privacy_status = self.retrieve_element_text_contains("warning_message_privacy_policy_xpath",
                                                             self.warning_message_privacy_policy_xpath,
                                                             expected_privacy_policy_message)
        first_name_status = self.retrieve_element_text_equals("warning_first_name_xpath", self.warning_first_name_xpath,
                                                              expected_first_name_warning)
        last_name_status = self.retrieve_element_text_equals("warning_last_name_xpath", self.warning_last_name_xpath,
                                                             expected_last_name_warning)
        email_status = self.retrieve_element_text_equals("warning_email_xpath", self.warning_email_xpath,
                                                         expected_email_warning)
        telephone_status = self.retrieve_element_text_equals("warning_telephone_xpath", self.warning_telephone_xpath,
                                                             expected_telephone_warning)
        password_status = self.retrieve_element_text_equals("warning_password_xpath", self.warning_password_xpath,
                                                            expected_password_xpath)
        return self.return_and_status(privacy_status, first_name_status, last_name_status, email_status,
                                      telephone_status, password_status)
