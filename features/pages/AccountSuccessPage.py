from features.pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_creation_xpath = "//div[@id='content']/h1"

    def successful_account_creation(self, account_creation_message):
        return self.retrieve_element_text_equals("account_creation_xpath", self.account_creation_xpath,
                                                  account_creation_message)
        # return self.driver.find_element(By.XPATH, self.account_creation).text.__eq__(account_creation_message)


