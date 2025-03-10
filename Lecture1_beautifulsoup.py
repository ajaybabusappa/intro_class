import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://google.com'
response = requests.get(url)

# Parse the content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extract the title of the page
title = soup.title.string
print('Title of the page:', title)

# Example: Extract all paragraph tags
paragraphs = soup.find_all('a')
for para in paragraphs:
    print(para.get_text())
