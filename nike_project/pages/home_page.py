from playwright.sync_api import expect


class HomePage():
    def __init__(self, page):
        self.page = page

    def shop_engineered_click(self):
        shop_engineered_button = self.page.locator('[aria-label="Shop"][href="https://www.nike.com/il/w/golf-23q9w"]').first
        shop_engineered_button.click()

    def search_item(self, item):
        search = self.page.locator('[id="gn-search-input"]')
        search.click()
        search.fill(item)
        search.press("Enter")
        element1 = self.page.locator('[class="product-card__subtitle"][role="link"]').first
        element2 = self.page.locator('[class="product-card__subtitle"][role="link"]').nth(1)
        return element1, element2

    def jordan_click(self):
        jordan_button_top_left = self.page.locator('[aria-label="Jordan"][data-testid="link"]')
        jordan_button_top_left.click()

    def bag_items_count(self):
        bag_items_count = self.page.locator('[title^="Bag Items:"]')
        return bag_items_count


    # buttons on the right



    def favourites_button(self):
        favourites_button = self.page.locator('[data-testid="favorite-button"]')
        favourites_button.click()

    def bag_items(self):
        bag_items = self.page.locator('[title^="Bag Items:"]')
        bag_items.click()

        results = self.page.get_by_role("option")
        return results

    # upper menu

    def find_a_store(self):
        find_a_store = self.page.locator('[data-testid="desktop-user-menu-item-message-0"]')
        find_a_store.click()

    def help_button(self):
        help_button = self.page.locator('[data-testid="desktop-user-menu-item-message-1"]')
        help_button.click()

    def join_us(self):
        join_us = self.page.locator('[data-testid="desktop-user-menu-item-message-2"]')
        join_us.click()

    def sign_in(self):
        sign_in = self.page.locator('[data-testid="desktop-user-menu-item-message-3"]')
        sign_in.click()

        email_input = self.page.locator('[id="username"]')
        return email_input


    # middle menu
    # elements found with first text and first out of many elements because
    # they are using a lot of elements with the same locators
    # needs a change if the order of elements will change in the future
    # the rest of the project not like that

    def all_buttons_click(self,category_name):
        button = self.page.locator(f'[class="menu-hover-trigger-link"]',has_text = category_name)
        button.click()

    def new_button_click(self):
        new_menu_button = self.page.locator("text=new")
        new_menu_button.first.click()

    def men_button_click(self):
        men_menu_button =self.page.locator("text=Men")
        men_menu_button.first.click()

    def women_button_click(self):
        women_menu_button =self.page.locator("text=Women")
        women_menu_button.first.click()

    def kids_button_click(self):
        kids_menu_button =self.page.locator("text=Kids")
        kids_menu_button.first.click()

    def sport_button_click(self):
         sport_menu_button =self.page.locator('[data-testid="link"][href="https://www.nike.com/il/lockerroom"]')
         sport_menu_button.click()




