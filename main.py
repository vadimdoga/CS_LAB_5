from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')

driver.get("http://www.google.com")

input_el = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
input_el.send_keys('computer')
input_el.send_keys(Keys.ENTER)

google_logo = driver.find_element_by_css_selector('#logo')
logo_display = google_logo.value_of_css_property('display')

assert 'block' == logo_display
