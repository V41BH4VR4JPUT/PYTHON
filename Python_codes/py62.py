# Request Module in Python

import requests
from bs4 import BeautifulSoup
url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)

# response = requests.get("https://www.google.com/")
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'Vaibhav',
#     "body": 'Rajput',
#     "userId": 7,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)