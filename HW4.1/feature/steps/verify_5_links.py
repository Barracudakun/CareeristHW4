from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Open amazon best seller page')
def open_amazon_bellerPage(context):
    context.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.implicitly_wait(10)


@then('Verify there are {expected_links} links')
def verify_links_count(context,expected_links):
    actual_links = context.driver.find_elements(By.CSS_SELECTOR, '#zg_tabs a')
    assert len(actual_links) == int(expected_links)
