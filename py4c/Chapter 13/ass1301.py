import urllib.parse, urllib.request, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input("Enter localtion: ")
    if len(url) < 1: break
    fh = urllib.request.urlopen(url)
    data = fh.read()
    tree = ET.fromstring(data)
    lst = tree.findall(".//count")
    print(sum(int(item.text) for item in lst))
