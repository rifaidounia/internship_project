Feature: tests for main menu bar

  Scenario: User can open market tab and add company option
    Given open reelly main page
    When log into page
    And Click on “market” in the left side menu
    Then verify right page opens
    When Click on “Agency” filter at the top of the page
    Then Verify all cards have the “Agency” tag


  Scenario: User can open market tab and add company option in mobile view
    Given open reelly main page
    When log into page
    And Click on “market” in bottom menu
    Then verify right page opens
    When Click on “Agency” filter at the top of the page
    Then Verify all cards have the “Agency” tag


