# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()
driver.get("https://www.heureka.cz")
driver.maximize_window()

#Navigating to the section Electronics/Mobile phones
el = driver.find_element_by_xpath('//*[@title="Elektronika"]')
el.click()
driver.implicitly_wait(5)
type = driver.find_element_by_link_text("Mobily, GPS").click()
driver.implicitly_wait(5)
type2 = driver.find_element_by_link_text("Mobilní telefony").click()

#Select the value in dropdown
select = Select(driver.find_element_by_id('order-top'))
select.select_by_value('5')

#The most expensive phone chosen
expensive = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/div[4]/div[3]/div[2]/div/h2/a")
expensive.click()

# Xpath not the best solution, tried to find by class, but unfortunately BUY button was not clicked
buy_button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/div[1]/table/tbody/tr/td[2]/div/div[3]/div[1]/div[1]/p/a")
buy_button.click()

#Closing pop-up window and navigating back to the Phones section
driver.find_element_by_xpath('//*[@title="Zavřít okno"]').click()
mobile_section = driver.find_element_by_link_text("Mobilní telefony").click()

#Dropdown selection
select = Select(driver.find_element_by_id('order-top'))
select.select_by_value('4')

#Found the second cheapest phone, because the 1st one is not on the Heureka, external webside
cheap = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/div[4]/div[5]/div[2]/div/h2/a")
cheap.click()

buy2 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/div[1]/table/tbody/tr/td[2]/div/div[3]/div[1]/div[1]/p/a")
buy2.click()





#type.click()




