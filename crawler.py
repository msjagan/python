import sys
import urllib
import re
import json

title = input("Enter the Title: ")
year = input("Enter the Year: ")

rw_str = re.compile(r' ')

searchstring = rw_str.sub('+', title)

print(searchstring)

url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

request = urllib.request(url)

response = json.load(urllib.urlopen(request))

print(response)


