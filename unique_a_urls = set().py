import requests
from bs4 import BeautifulSoup

# URL we are trying to scrape
url = "https://www.google.co.in/?safe=active&ssui=on"

# Sending a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Webpage fetched successfully.")
    content = response.text
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    content = ""

# Parsing the content with BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Finding all <a> tags and <img> tags
a_tags = soup.find_all('a')
img_tags = soup.find_all('img')

# Using sets to store unique URLs
unique_a_urls = set()
unique_img_urls = set()

# Extracting href attributes from <a> tags
for tag in a_tags:
    href = tag.get('href')
    if href:
        unique_a_urls.add(href)

# Extracting src attributes from <img> tags
for tag in img_tags:
    src = tag.get('src')
    if src:
        unique_img_urls.add(src)

# Printing unique URLs from <a> tags
print("Unique A Tag URLs:")
for url in unique_a_urls:
    print(url)

# Printing unique Image URLs from <img> tags
print("Unique Image URLs:")
for url in unique_img_urls:
    print(url)