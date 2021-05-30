from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config.constants import DEFAULT_WAIT_TIME


class MoatHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://moat.com'

    # locators
    search_bar_loc = (By.ID, 'adsearch-input')
    dropdown_list_loc = (By.XPATH, '//span[@class="non-query-string"]')

    # property

    @property
    def search_bar(self):
        return self.driver.find_element(*self.search_bar_loc)

    @property
    def dropdown_list(self):
        wait = WebDriverWait(self.driver, DEFAULT_WAIT_TIME)
        wait.until(expected_conditions.presence_of_element_located(self.dropdown_list_loc))
        return self.driver.find_elements(*self.dropdown_list_loc)

    @property
    def first_autocomplete_dropdown_value(self):
        wait = WebDriverWait(self.driver, DEFAULT_WAIT_TIME)
        wait.until(expected_conditions.presence_of_element_located(self.dropdown_list_loc))
        return self.driver.find_elements(*self.dropdown_list_loc)[0]

    # methods
    def assert_page_loaded(self):
        """asserts the page is loaded"""
        wait = WebDriverWait(self.driver, DEFAULT_WAIT_TIME)
        wait.until(expected_conditions.presence_of_element_located(self.search_bar_loc))
