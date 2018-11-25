# Written by Johnathan Graydon
# Scrape the metmuseum api for all portraits in the public domain
import json
import requests
import urllib
import time

with open('ObjectsToUse.csv', 'rb') as f:
    objectList = f.read().splitlines()

# apiMax = 818235

from urllib import FancyURLopener

class MyOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

myopener = MyOpener()

for object in objectList:

    print("Downloading " + object)

    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(object))
    data = json.loads(response.content)
    time.sleep(1)
    if data["primaryImage"] != "":
        print(data["primaryImage"])

        myopener.retrieve(data["primaryImage"], "images/" + str(object) + ".jpg")
        # urllib.urlretrieve(data["primaryImage"], "images/" + str(object) + ".jpg")
