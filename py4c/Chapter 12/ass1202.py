# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
#for tag in tags:
print("Retrieve:", url)
time = 1
while time <= count:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    tags = soup('a')
    tag = tags[pos - 1]
    url = tag.get("href", None)
    print("Retrieve:", url)
    #print("Retrieve:", tag.get("href", None))
    time = time + 1
