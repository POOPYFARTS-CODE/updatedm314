from logging import error
from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def nike(link,size,ac_email,ac_psk,pan):
  driver = webdriver.Chrome("chromedriver.exe")
  driver.get(link)
  if size == 5:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635978']").click()
  elif size == 5.5:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635990").click()
  elif size == 6:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635985']").click()
  elif size == 6.5:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635988']").click()
  elif size == 7:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635984']").click()
  elif size == 7.5:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635981']").click()
  elif size == 8:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635983']").click()
  elif size == 8.5:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635980']").click()
  elif size == 9:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635982']").click()
  elif size == 9.5:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635979']").click()
  elif size == 10:
     driver.find_element_by_xpath("//label[@for='skuAndSize__25635992']").click()
  else:
    print("Invalid Size Or Size Not Available!")
  
  driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[3]/div[2]/div/div/div[2]/form/div[2]/div/div/button[1]').click()
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="PDP"]/div/div[4]/div/div/div/div/div/div/div/div/div/div[3]/div/button[2]')
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="react-root"]/div/div[4]/button').click()
  driver.find_element_by_xpath('//*[@id="e454e896-1928-4c57-a78e-87102356fe3f"]').send_keys(ac_email)
  driver.find_element_by_xpath('//*[@id="69e11f3a-d6d5-4482-87ce-ca523ec3b038"]').send_keys(ac_psk)
  driver.find_element_by_xpath('//*[@id="bad07a40-7982-4952-94b8-dee5eb8bedd6"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('//*[@id="gdprSection"]/div[1]/label[1]/span').click()
  driver.find_element_by_xpath('//*[@id="governmentid"]').send_keys(pan)
  driver.find_element_by_xpath('//*[@id="shippingSubmit"]').click()
  driver.find_element_by_xpath('//*[@id="billingSubmit"]').click()
  time.sleep(5)

