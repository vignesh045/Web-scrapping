import requests;
from bs4 import BeautifulSoup;
url="https://www.google.co.in/?safe=active&ssui=on" # Url we are trying to scrap
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    content = response.text
    print("Webpage fetched successfully.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    content= ""
soup=BeautifulSoup(content,'lxml')

atag=soup.find_all('a')
imgtag=soup.find_all('img')
set_atag=set()
set_imgtag=set()
for i in imgtag:
    img_url= i.get('src')
    if img_url:
        set_imgtag.add(img_url)
for a in atag:
    a_url=a.get('href')
    if a_url:
        set_atag.add(a_url)
print(" Unique image links are below")

for j in set_imgtag:
    print(j)

with open('ImageUnique.txt', 'w') as file:
    for i in imgtag:
        img_url= i.get('src')
        if img_url:
            file.write(img_url + '\n')
print(" Unique atag links are below\n")

for k in atag:
    print(k)

with open('AtagUnique.txt', 'w') as file:
            for a in atag:
                 a_url=a.get('href')
                 if a_url:
                      file.write(a_url + '\n')