Feature: Login Positive

Scenario Outline: User want Login to system using registered account
Given User go to secondhand website
When User input email "<email>"
And User input password "<password>"
And User click Masuk button
Then User successfully login

Examples:
    | email                 | password     |
    | binarqae1@gmail.com   | students1234 |

Scenario Outline: User want Login to system using wrong account
Given User go to secondhand website
When User input email "<email>"
And User input password "<password>"
And User click Masuk button
Then User successfully login

Examples:
    | email                 | password     |
    | binarqae12@gmail.com  | students1234 |