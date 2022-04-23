from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_to_items(self):
        # Edith goes to the home page and accidently tries to submit and empty list item.
        # She hits enter on the empty input box.

        # The home page refreshes and there is an error message saying that the list items cannot be blank.

        # She tries again with some text for the item which now works.

        # Perversely, she now decides to submit a second blank list item.

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in

        self.fail("Write me!")