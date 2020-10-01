import urllib.parse, urllib.request, urllib.error
import ssl
import json

# Ignore SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input("Enter location: ")
    if len(url) < 1: break
    fh = urllib.request.urlopen(url)
    data = fh.read()
    info = json.loads(data)
    #print(info["comments"][1]["count"])
    lst = info["comments"]
    print(sum(int(item["count"]) for item in lst))
