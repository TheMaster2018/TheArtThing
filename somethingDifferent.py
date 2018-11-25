# Written by Oliver Gledhill
# Goes through a file containing image file names and adds it all to an aws rekognition image collection
import os

with open('keys.txt', 'rb') as f:
    objectList = f.read().splitlines()

for object in objectList:
    print("Adding " + object + " to AWS Image Collection...")

    os.system("python aws rekognition index-faces --image '" + "{" + '"S3Object"' + ':{' + '"Bucket":"artrecognition2","Name":"' + object + '"' + "}}'" + '  --collection-id "referenceImages"  --max-faces 1  --quality-filter "AUTO"  --detection-attributes "ALL"  --external-image-id "' + object + '"')
