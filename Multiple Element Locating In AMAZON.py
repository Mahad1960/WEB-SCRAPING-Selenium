from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query="laptop"                                # You can also take input here.
for i in range(1,4):                          # It will search for 3 pages.
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=23Z9HPBL2JMRH&qid=1753079127&sprefix=%2Caps%2C660&xpid=yyORC7MGEp591&ref=sr_pg_{i}")
    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")  
    for elem in elems:
        print(elem.text) 
    print("\n")
    print(f"{len(elems)} items found on page {i}.\n")
    time.sleep(4)
driver.close()