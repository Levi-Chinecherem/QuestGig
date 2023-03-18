# for running single request

import json
import time
import requests
from bs4 import BeautifulSoup

site_link = requests.get(input("enter url: "))
site_content = BeautifulSoup(site_link.content, 'html.parser')
string_content = str(site_content)


# Data to be written
site = {
  "website": f"{str(string_content)}"
}


# Serializing json
json_object = json.dumps(site, indent=2)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
  outfile.write(json_object)

print("Done!!!") 
