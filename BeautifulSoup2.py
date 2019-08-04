import urllib
from BeautifulSoup import *

URL = input("Enter the URL:")
link_line = int(input("Enter position:")) - 1 #In this question  18
count = int(input("Enter count:"))  # In this question 7

while count >= 0:
    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print(URL)
    URL = tags.get("href", None)
    count = count - 1
