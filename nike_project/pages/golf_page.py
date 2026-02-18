class GolfPage():
    def __init__(self, page):
        self.page = page

    def click_category_and_gender(self,category):
        category_option = self.page.locator('.categories__content').locator(f'[aria-label="Category for {category}"]')
        category_option.click()

    def choose_gender_golf(self,option):
        gender_options = self.page.get_by_role("button").locator('[aria-label="Gender"]')
        gender_options.click()
        gender_option = self.page.get_by_label(f"Filter for {option}")
        gender_option.click()



