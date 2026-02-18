import pytest
from playwright.sync_api import expect


class page_after_search_item():
    def __init__(self,page):
        self.page = page

    def click_on_item_and_pick_size(self,size):
        item = self.page.locator('[id="skip-to-products"]').first
        item.click()
        size = self.page.locator(f'[for="grid-selector-input-{size}"]')
        if size.is_enabled():
            size.click()
        else:
            pytest.skip(f"Size {size} not available")


        # cant do the next 2 lines it will create error message because im a bot
        # add_to_bag_button = self.page.get_by_role("button",name = "Add to Bag")
        # add_to_bag_button.click()

    def home_button(self):
        home_button = self.page.locator('[aria-label="Nike Homepage"][data-testid="link"]')
        home_button.click()

    def choose_gender_after_search(self, option):
        gender_options = self.page.get_by_role("button").locator('[aria-label="Gender"]')
        gender_options.click()
        gender_option = self.page.get_by_label(f"Filter for {option}")
        gender_option.click()

    def sort_after_item_search(self,option_name):
        sort_button = self.page.locator('[id="dropdown-btn"]')
        sort_button.click()
        option = self.page.get_by_role('menuitem',name=option_name)
        option.click()
        after_select = self.page.locator('[class="dropdown__btn-selected-text"]',has_text =option_name)
        return after_select

    def pick_a_color(self,first_color,second_color):
        colors = self.page.locator('[aria-label="Colour"]').locator('[class="trigger-content__label"]')
        colors.click()
        color_choice_1 = self.page.locator(f'[aria-label="Filter for {first_color}"]')
        color_choice_1.click()
        expect(color_choice_1).to_have_attribute("class","filter-item is--color is--selected is--button css-5faxmh")
        color_choice_2 = self.page.locator(f'[aria-label="Filter for {second_color}"]')
        color_choice_2.click()
        expect(color_choice_2).to_have_attribute("class", "filter-item is--color is--selected is--button css-5faxmh")
        return color_choice_1,color_choice_2



