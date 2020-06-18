#%% Imports and inis

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import datetime
from selenium import webdriver

#%%

url = 'https://www.italki.com/teachers/english?page=2'

# %% Get into google driver

path = r'C:\Users\dougl\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.get(url)

# %% Get api 
page_num=500
api_url = r'https://www.italki.com/api/v2/teachers?page_size=99&page={}'.format(page_num)

# %% 
response = requests.get(api_url)
# Print the status code of the response.
print(response.status_code)

data = response.json()
data

# %%
