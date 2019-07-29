import urllib.request
from bs4 import BeautifulSoup

file = "http://py4e-data.dr-chuck.net/comments_254949.html"
fh = urllib.request.urlopen(file)
soup = BeautifulSoup(fh, "html.parser")

spans = soup('span')

count = []

for span in spans:
    count.append(int(span.string))
    
print(sum(count))
