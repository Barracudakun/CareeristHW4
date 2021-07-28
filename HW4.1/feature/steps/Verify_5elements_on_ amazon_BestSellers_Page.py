from behave import *
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


@given('Open amazon best seller page')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Find Best Sellers,New Releases,Movers & Shakers, Most Wished For , Gift Ideas elements')
def step_impl(context):
    context.find_element(By.CSS_SELECTOR, ".zg_selected a")
    context.find_element(By.CSS_SELECTOR, "")

@then(u'verify there are 5 links: Best Sellers,New Releases,Movers & Shakers, Most Wished For , Gift Ideas on the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify there are 5 links: Best Sellers,New Releases,Movers & Shakers, Most Wished For , Gift Ideas on the page')
