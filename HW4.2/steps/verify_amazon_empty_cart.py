from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver

@when(u'Click on cart icon')
def click_cart(context):
    # context.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
    context.driver.find_element(By.ID, 'nav-cart').click()

@then('{expected_text} message is displayed')
def verify_empty_cart_msg(context, expected_text):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '#sc-active-cart h2').text
    assert actual_text == expected_text, f'Expected{expected_text}, but got {actual_text}'