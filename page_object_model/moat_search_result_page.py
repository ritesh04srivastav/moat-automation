from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config.constants import DEFAULT_WAIT_TIME, CREATIVE_COUNTS


class MoatSearchResultPage:

    def __init__(self, driver):
        self.driver = driver

    # locators
    creative_count_loc = (By.XPATH, '//div[@class="creative-count"]')
    random_brand_hyperlink_loc = (By.LINK_TEXT, 'Random Brand')
    search_result_loc = (By.XPATH, '//div[@class="er-creative  "]')
    share_loc = (By.LINK_TEXT, 'Share')

    # property

    @property
    def creative_count(self):
        wait = WebDriverWait(self.driver, DEFAULT_WAIT_TIME)
        wait.until(expected_conditions.presence_of_element_located(self.creative_count_loc))
        return self.driver.find_element(*self.creative_count_loc)

    @property
    def random_brand_hyperlink(self):
        wait = WebDriverWait(self.driver, DEFAULT_WAIT_TIME)
        wait.until(expected_conditions.presence_of_element_located(self.random_brand_hyperlink_loc))
        return self.driver.find_element(*self.random_brand_hyperlink_loc)

    @property
    def first_search_result(self):
        wait = WebDriverWait(self.driver, DEFAULT_WAIT_TIME)
        wait.until(expected_conditions.presence_of_element_located(self.search_result_loc))
        return self.driver.find_elements(*self.search_result_loc)[0]

    @property
    def share(self):
        return self.driver.find_element(*self.share_loc)

    # methods
    def assert_page_loaded(self):
        """Validates if page loaded successfully"""
        assert self.random_brand_hyperlink.is_displayed()

    def validate_creative_count(self, search_term_text):
        """Validates if creative count for searched term matches"""
        search_header_loc = (By.XPATH, '//span[text()="{}"]'.format(search_term_text))

        wait = WebDriverWait(self.driver, DEFAULT_WAIT_TIME)
        wait.until(expected_conditions.presence_of_element_located(search_header_loc))
        wait.until(expected_conditions.presence_of_element_located(self.search_result_loc))

        if search_term_text == 'Saturn': search_term_text = 'saturn'
        elif search_term_text == "Saturday's Market": search_term_text = 'saturdays_market'
        elif search_term_text == "Krux": search_term_text = 'krux'

        assert self.creative_count.text == CREATIVE_COUNTS[search_term_text]

    def validate_random_brand_link(self):
        """Validates random brand link is random"""
        random_number = 5
        random_hyperlink_list = []
        for i in range(0, random_number):
            self.random_brand_hyperlink.click()
            random_hyperlink_list.append(self.driver.current_url)

        for j in range(1, len(random_hyperlink_list)):
            assert random_hyperlink_list[j-1] != random_hyperlink_list[j]

    def hover_search_result(self):
        """Hovers to the element"""
        ActionChains(self.driver).move_to_element(self.first_search_result).perform()

    def validate_share(self):
        """asserts to share link"""
        assert self.share.is_displayed()