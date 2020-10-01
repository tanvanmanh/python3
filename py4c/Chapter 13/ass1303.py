import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore ssl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    params = dict()
    params["address"] = address
    if api_key is not False: params["key"] = api_key
    url = serviceurl + urllib.parse.urlencode(params)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    print("Place id", info["results"][0]["place_id"])
