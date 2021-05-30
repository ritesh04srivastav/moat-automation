import pytest
from selenium import webdriver
from pytest_bdd import given, when, then, parsers
from config.constants import CHROME_PATH, DEFAULT_SEARCH_TERM
from page_object_model.moat_home_page import MoatHomePage
from page_object_model.moat_search_result_page import MoatSearchResultPage


@pytest.fixture
def page_objects():
    """Dictionary to hold page objects"""
    return {}


@pytest.fixture
def driver():
    """initiates browser driver and quits at the end of the tests"""
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()


@given('I have moat_home')
def moat_home(page_objects, driver):
    """Instantiates the page Object for Maot home page"""
    page_objects['moat_home_page'] = MoatHomePage(driver)


@given('I have moat_search_result_page')
def moat_home(page_objects, driver):
    """Instantiates the page Object for Maot search result page"""
    page_objects['moat_search_result_page'] = MoatSearchResultPage(driver)


@given(parsers.parse('I load the {page_name}'))
def load_page(page_objects, driver, page_name):
    """loads the desired page"""
    driver.get(page_objects[page_name].url)
    page_objects[page_name].assert_page_loaded()


@when(parsers.parse('I see the {page_name}'))
def see_element(page_objects, page_name):
    """Validates the desired page"""
    page_objects[page_name].assert_page_loaded()


@when(parsers.parse('I see the {element_name} on the {page_name}'))
def see_element(page_objects, page_name):
    """Validates the desired element on the page"""
    page_objects[page_name].assert_page_loaded()


@when('I fill out default search term on the moat_home_page')
def default_search_term(page_objects):
    """fills with default search term"""
    page_objects['moat_home_page'].search_bar.send_keys(DEFAULT_SEARCH_TERM)


@when('I fill out search term as <search_term_text> on the moat_home_page')
def default_search_term(page_objects, search_term_text):
    """fills with user provided search term"""
    page_objects['moat_home_page'].search_bar.send_keys(search_term_text)


@when(parsers.parse('I click the {element} on the {page_name}'))
def click(page_objects, page_name, element):
    """clicks the element of the page"""
    element = getattr(page_objects[page_name], element)
    element.click()


@when('I hover on random search results on the moat_search_result_page')
def hover_search_result(page_objects):
    """hovers the element of the page"""
    page_objects['moat_search_result_page'].hover_search_result()


@then(parsers.parse('I validate autocomplete_drop_down_list on the {page_name}'))
def validate_default_dropdown(page_objects, page_name):
    """validates the auto search elements of the page"""
    autocomplete_drop_down_list = page_objects[page_name].dropdown_list
    for dropdown_value in autocomplete_drop_down_list:
        assert 'test' in dropdown_value.text.lower() or 'complete' in dropdown_value.text.lower()


@then(parsers.parse('I validate creatives_count for <search_term_text> on the moat_search_result_page'))
def creative_count(page_objects,search_term_text):
    """validates the creative search count for the searched term of the page"""
    page_objects['moat_search_result_page'].validate_creative_count(search_term_text)


@then('I validate random_brand_link is random on the moat_search_result_page')
def random_brand_link(page_objects):
    """validates the random brand link"""
    page_objects['moat_search_result_page'].validate_random_brand_link()


@then('I validate share_link on the moat_search_result_page')
def share(page_objects):
    """validates share"""
    page_objects['moat_search_result_page'].validate_share()
