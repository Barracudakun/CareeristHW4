from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open amazon page')
def open_amazon(context):
    context.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
    context.driver.get('https://www.amazon.com')
    context.driver.implicitly_wait(10)

@when('Search for {search_word}')
def search_for_laptop(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word, Keys.RETURN)

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.a-size-base-plus.a-color-base.a-text-normal').click()


@when('Click on Add to cart button')
def click_add_to_cart_button(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify cart has {expected_number} item')
def verify_cart_number(context, expected_number):
    actual_number = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert expected_number == actual_number, f'{expected_number} but got {actual_number}'

