Feature: Bestsellers tests

  Scenario: There are 5 bestsellers links
    Given Open amazon best seller page
    Then verify there are 5 links

