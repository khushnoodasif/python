import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'http://www.example.com'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the data you want to extract
data = soup.find(...)

# Extract the data and store it in a variable or save it to a file
result = data.text
