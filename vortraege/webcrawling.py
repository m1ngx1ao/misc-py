import requests
import regex
html = requests.get('https://cispa.de/de/people').text
people = regex.findall(r'".+">(.+)</option>', html)
for p in people:
	html = requests.get('https://cispa.de/de/people/' + p).text
	tel = regex.findall(r'".+">(.+)</option>', html)
tels = []
tels += tel

print(tels)
print("Mitarbeiteranzahl: " + str(len(people)))