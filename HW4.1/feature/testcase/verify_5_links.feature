Feature: Verify 5 elements on the amazon BestSellers Page

  Scenario: verify there are 5 links: Best Sellers,New Releases,Movers & Shakers, Most Wished For , Gift Ideas on the page
    Given Open amazon best seller page
    When Find Best Sellers,New Releases,Movers & Shakers, Most Wished For , Gift Ideas elements
    Then verify there are 5 links: Best Sellers,New Releases,Movers & Shakers, Most Wished For , Gift Ideas on the page

