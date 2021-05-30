@ritesh
Feature: tests to automate moat functionalities


  Scenario: Verify the search bar autocomplete drop down text.
    Given I have moat_home
    And I load the moat_home_page
    When I see the search_bar on the moat_home_page
    And I fill out default search term on the moat_home_page
    Then I validate autocomplete_drop_down_list on the moat_home_page

  Scenario Outline: Verify the creatives count on the search results page
    Given I have moat_home
    And I have moat_search_result_page
    And I load the moat_home_page
    When I see the search_bar on the moat_home_page
    And I fill out search term as <search_term_text> on the moat_home_page
    And I click the first_autocomplete_dropdown_value on the moat_home_page
    And I see the moat_search_result_page
    Then I validate creatives_count for <search_term_text> on the moat_search_result_page

    Examples:
      |search_term_text |
      |Saturn           |
      |Saturday's Market|
      |Krux             |


  Scenario: Verify the Random Brand link on the search results page is random.
    Given I have moat_home
    And I have moat_search_result_page
    And I load the moat_home_page
    When I see the search_bar on the moat_home_page
    And I fill out default search term on the moat_home_page
    And I click the first_autocomplete_dropdown_value on the moat_home_page
    And I see the moat_search_result_page
    Then I validate random_brand_link is random on the moat_search_result_page


  Scenario: Verify the Share ad feature (it appears on overlay when hovering over an ad)
    Given I have moat_home
    And I have moat_search_result_page
    And I load the moat_home_page
    When I see the search_bar on the moat_home_page
    And I fill out default search term on the moat_home_page
    And I click the first_autocomplete_dropdown_value on the moat_home_page
    And I see the moat_search_result_page
    And I hover on random search results on the moat_search_result_page
    Then I validate share_link on the moat_search_result_page

