## Using beautifulsoup to prettify html doc:

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

##

# Getting some data from the page 

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)


##

# Turning a webpage into data, getting the hyperlinks

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a') # a_tags is a result set, I'm assuming this maintains its props, each element prolly has methods and what not on it

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href')) # get accesses the attributes ? 