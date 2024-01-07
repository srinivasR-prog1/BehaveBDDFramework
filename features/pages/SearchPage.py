from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    display_product_link_text = "HP LP3065"
    no_matches_found_message_xpath = "//input[@id = 'button-search']/following-sibling::p"

    def display_valid_product_search(self):
        return self.display_status("display_product_link_text", self.display_product_link_text)

    def display_message_search_results(self, expected_text_message):
        return self.retrieve_element_text_equals("no_matches_found_message_xpath", self.no_matches_found_message_xpath,
                                                 expected_text_message)
