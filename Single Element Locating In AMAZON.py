# FOR INSTALLATION : pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=2YQQX92WQ8HLU&sprefix=laptop%2Caps%2C520&ref=nb_sb_noss_2")
elem = driver.find_element(By.CLASS_NAME,"puis-card-container")   
print(elem.text)                         # This will get me the text of above line.
print(elem.get_attribute("outerHTML"))   # This will provide me the "Outer Html" of above line.
time.sleep(6)
driver.close()