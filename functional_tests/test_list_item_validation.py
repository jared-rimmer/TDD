from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_to_items(self):
        # Edith goes to the home page and accidently tries to submit and empty list item.
        # She hits enter on the empty input box.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request and does not load the list page
        self.wait_for(
            lambda: self.browser.find_element(
                by=By.CSS_SELECTOR, value="#id_text:invalid"
            ).text
        )

        # She starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys("Buy milk")
        self.wait_for(
            lambda: self.browser.find_element(
                by=By.CSS_SELECTOR, value="#id_text:valid"
            ).text
        )

        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(row_text="1: Buy milk")

        # Perversely, she now decides to submit a second blank list item.
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.wait_for(
            lambda: self.browser.find_element(
                by=By.CSS_SELECTOR, value="#id_text:invalid"
            ).text
        )
        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys("Make tea")
        self.wait_for(
            lambda: self.browser.find_element(
                by=By.CSS_SELECTOR, value="#id_text:valid"
            ).text
        )

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(row_text="1: Buy milk")
        self.wait_for_row_in_list_table(row_text="2: Make tea")
