# Import all the libraries used for the scraping
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re


# Function to call the website and get both name and purpose of the company
def webscrap(p):
    page = requests.get(p)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        name = soup.find(text=re.compile("Name")).lstrip("nName:")
        purpose = soup.find(text=re.compile("Purpose")).lstrip("pPurpose:")
        datasave = {"name": name, "purpose": purpose}
    else:
        print("Cannot Connect")
    return datasave


# Create a dataframe to store the name and purpose of 50 companies
end_data = pd.DataFrame(columns=["name", "purpose"], index=range(0, 50))

# Cycle to make 50 requests to the website and save name and purpose to the table created above
for i in range(0, 50):
    end_data.iloc[i] = webscrap("http://18.207.92.139:8000/random_company")
    time.sleep(0.5)

# Save resulting table as .csv file
end_data.to_csv("companies.csv")
