
<p align="center">
  <img src="https://github.com/Levi-Chinecherem/QuestGig/blob/main/photos/crawler_logo.PNG" width="1000" alt="web crawler" title="questgig web crawler">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/QuestGig-Crawler%2FBot-blueviolet" width="350" title="the questgig bot">
  <img src="https://img.shields.io/badge/QuestGig-Web%20Crawler-blueviolet" width="350" alt="web crawler" title="questgig web crawler">
</p>

in this questgib sub project we are building a web crawler which returnd the following
* the website html
* the contents (videos, text, images, audios etc)
* returns you with links embedded in such site too

### caution
* this bot returns everything about the site from html(opening) to html(closing tag)
* you will have to extract the contents according to your needs
* have a purpose for using this bot as it can serve as a clonner for you

## future upgrade
* ability to saparate returned content according to its category (vdeos, images, text, etc)

## Guide
* bot.py contains code to get content from list of given websites
* questBot.py only gets the content of any website given to it during run time
* to run this project ensure to pip install requests, pandas, and BeautifulSoup 4
* results are returned in json format and it returns the name in time seconds so always check the name 
* use the readfile.py to read the returned json file, remember to always change the name to the current json file
