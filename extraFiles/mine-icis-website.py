import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://aisel.aisnet.org/icis2014/")

tracks=driver.find_element_by_partial_link_text('Conference Theme Track')
url=tracks.get_attribute('href')
driver.get(url)

