info = open("info.txt").readlines()
info = list(map(lambda x:x.strip(),info))
email = info[0]
first_n = info[1]
last_n = info[2]
addres_line1 = info[3]
addres_line2 = info[4]
city = info[6]
zip = info[5]
phone_no = info[6]
paypal_pass = info[7]

from socket import if_indextoname
from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time



def supreme(link ,size):
  global email,first_n,last_n,addres_line1,addres_line2,city,zip,phone,paypal_pass
    
  driver = webdriver.Chrome("chromedriver.exe" )
  driver.get(link)
  time.sleep(5)
   
  if size == "s":
   driver.find_element_by_xpath("//label[@for='swatch-0-s']").click()
   print('Succes')
  elif size == "m":
    driver.find_element_by_xpath("//label[@for='swatch-0-m']").click()
    print('Succes')
  elif size == "l":
    driver.find_element_by_xpath("//label[@for='swatch-0-l']").click()
    print('Succes')
  elif size == "xl":
    driver.find_element_by_xpath("//label[@for='swatch-0-xl']").click()
    print('Succes')
  else:
    print("Invalid Size Or Size Not Available!")


    time.sleep(5)
    element2 = driver.find_element_by_xpath("/html/body/div[4]/main/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/form/div[5]/input")
    element2.click()
    time.sleep(10)
    element3 = driver.find_element_by_xpath("//BUTTON[@class='btn btn-go-to-cart'][text()='Go to cart']")
    time.sleep(5)
    element3.click()
    element4 = driver.find_element_by_xpath('/html/body/div[4]/main/div/div/div/form/div[2]/div[3]/input')
    element4.click()
    time.sleep(5)
    email_duda = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/input')
    email_duda.send_keys(email)
    name1 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/input')
    name1.send_keys(first_n)
    name2 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/input')
    name2.send_keys(last_n)
    addres = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/input')
    addres.send_keys(addres_line1)
    addres2 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/input')
    addres2.send_keys(addres_line2)
    addres3 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[5]/div/input')
    addres3.send_keys(city)
    time.sleep(5)
    dropdown = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]').click()
    pin = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[8]/div/input')
    pin.send_keys(zip)
    phone = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[9]/div/input')
    phone.send_keys(phone)
    continue_ = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[2]/button')
    continue_.click()
    time.sleep(5)
    continue_1 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[2]/button')
    continue_1.click()
    time.sleep(5)
    check_box = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[4]/div[1]/input')
    check_box.click()
    time.sleep(10)
    btnlast = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/div/form/div[3]/div[1]/button')
    btnlast.click()
    time.sleep(10)
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(paypal_pass)
    time.sleep(10)
