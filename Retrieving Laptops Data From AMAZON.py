import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
ua=UserAgent().random
options = Options()
options.add_argument(f"--user-agent={ua}")   # This line should be in this format.
driver = webdriver.Chrome(options=options)
query="laptop"                                # You can also take input here.
j=1
for i in range(1,4):                          # It will search for 3 pages.
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=23Z9HPBL2JMRH&qid=1753079127&sprefix=%2Caps%2C660&xpid=yyORC7MGEp591&ref=sr_pg_{i}")
    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")  
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"AMAZON LAPTOPS DATA/{query}{j}.html","w",encoding="utf-8") as f:
            f.write(d)
            j+=1
    print("\n")
    print(f"{len(elems)} items found on page {i}.")
    time.sleep(4)
driver.close()