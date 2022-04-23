from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_to_items(self):
        # Edith goes to the home page and accidently tries to submit and empty list item.
        # She hits enter on the empty input box.
        self.browser.get(self.live_server_url)
        self.browser.find_element(by=By.ID, value="id_new_item").send_keys(Keys.ENTER)

        # The home page refreshes and there is an error message saying that the list items cannot be blank.
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(by=By.CSS_SELECTOR, value=".has-error").text,
                "You can't have an empty list items",
            )
        )
        # She tries again with some text for the item which now works.
        self.browser.find_element(by=By.ID, value="id_new_item").send_keys("Buy milk")
        self.browser.find_element(by=By.ID, value="id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(row_text="1: Buy milk")

        # Perversely, she now decides to submit a second blank list item.
        self.browser.find_element(by=By.ID, value="id_new_item").send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(by=By.CSS_SELECTOR, value=".has-error").text,
                "You can't have an empty list items",
            )
        )
        # And she can correct it by filling some text in
        self.browser.find_element(by=By.ID, value="id_new_item").send_keys("Make tea")
        self.browser.find_element(by=By.ID, value="id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(row_text="1: Buy milk")
        self.wait_for_row_in_list_table(row_text="1: Make tea")
