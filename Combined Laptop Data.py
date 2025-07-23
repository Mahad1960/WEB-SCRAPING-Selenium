from bs4 import BeautifulSoup
import os
import pandas as pd
d= {"title":[],"price":[],"link":[]}  # This method is used for creating CSV (Tabular Form).
combined_data = ""   # Initialize the combined data variable before the loop.
for file in os.listdir("AMAZON LAPTOPS DATA"):
# I have used "try" because if required text is missing in file it will only print exception and wouldn't stop the code.
    try:
        with open(f"AMAZON LAPTOPS DATA/{file}",encoding="utf-8") as f:
            doc=f.read()
        soup=BeautifulSoup(doc,"html.parser")
        t=soup.find("h2")
        title=t.get_text()
        # print("TITLE:",title,"\n")
        # l1=t.find("a")    # Looks for the first <a> inside the <h2>.
        # link1=l1["href"]  # It will get the href attribute (the link), and prints it.
        l2=soup.find("a")   # Looks for the first <a> inside the file.
        link2=l2["href"]    # It will print the href attribute (the link) in the file.
        # print("LINK",link2,"\n")
        s=soup.find("span",attrs={"class":"a-price-whole"})  # It returns the first <span> tag that has class "a-price-whole". It prints the whole HTML of that span tag.
        # print("SPAN:",s)
        price=s.get_text()
        # print("SPAN TEXT:",price)  # It will provide me the text of span.
        # The following steps will be created in CSV.
        d["title"].append(title)
        d["price"].append(price)
        d["link"].append(link2)
        # print(soup.prettify())
        # combined_data += soup.prettify() + "\n\n"   # "\n\n" adds two newline characters after each HTML block from a file.
    except Exception as e:
        print("EXCEPTION:",e)
df=pd.DataFrame(data=d)
df.to_csv("AMAZON LAPTOPS DATA (CSV FORMAT).csv")  # This will create a file.
# if(not os.path.exists("Data")):  
#   os.mkdir("AMAZON LAPTOPS COMBINED DATA")
# with open("AMAZON LAPTOPS COMBINED DATA/Laptops Data.html", "w", encoding="utf-8") as f:
#     f.write(combined_data)
