from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")

name = []
artist = []

driver.get("https://blogtruyen.vn/25011/sousou-no-frieren")
link = driver.current_url
# print(link)

# print(driver)
content = driver.page_source
soup = bs(content, features="html.parser")
# print(content)
# print("-----\n-----\n-----\n-----\n-----\n-----\n-----\n-----\n-----\n-----\n-----\n-----\n-----")
# print(soup)

