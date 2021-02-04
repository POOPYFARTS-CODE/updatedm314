

from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def adidas(link):
  driver = webdriver.Chrome("chromedriver.exe" )
  driver.get(link)
  time.sleep(10)
  element1 = driver.find_element_by_xpath("/html/body/div[20]/div[3]/div[1]/div/div[1]/div[3]/div[12]/div[1]/div/label[1]")
  element1.click()
  time.sleep(10)
  element2 = driver.find_element_by_xpath("/html/body/div[20]/div[3]/div[1]/div/div[1]/div[3]/div[19]/button")
  element2.click()
  time.sleep(15)
  element3 = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[1]/div[2]/div[2]/div[2]/a/button")
  element3.click()



  #            *     ,MMM8&&&.            *
  #                 MMMM88&&&&&    .
  #                MMMM88&&&&&&&
  #    *           MMM88&&&&&&&&
  #                MMM88&&&&&&&&
  #                'MMM88&&&&&&'
  #                  'MMM8&&&'      *
  #         |\___/|
  #         )     (             .              '
  #        =\     /=
  #          )===(       *
  #         /     \
  #         |     |
  #        /       \
  #        \       /
  # _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  # |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  # |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  # |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
