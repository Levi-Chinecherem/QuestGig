# for running multiple request
import time
import requests
from bs4 import BeautifulSoup

# list of sites to traverse on
links = [
  "https://github.com/Levi-Chinecherem", 
  "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#unlock", 
  "https://www.paypal.com", 
  "https://shoprite.ng"
  ]

counter = len(links) + 1

for link in links:
  site_link = requests.get(link)
  site_content = BeautifulSoup(site_link.content, 'html.parser')
  string_content = str(site_content)

  # Data to be written
  site = {
    "website": f"{str(string_content)}"
  }
  
  # Serializing json
  json_object = json.dumps(site, indent=4)

  # Writing to sample.json
  with open(f"site{int(time.time())}.json", "w") as outfile:
    outfile.write(json_object)
  
  # when done copying site data print done
  print(f"Done!!! {counter}")
  counter += 1
print("Successfully done with all given links")
 



 

