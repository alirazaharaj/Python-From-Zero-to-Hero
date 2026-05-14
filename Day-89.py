'''Request sa ham different type ki request mar sakta ha or phit bs4 nam ki libarary sa ham us page sa different text ko purify kar sakta ha '''

import requests
from bs4 import BeautifulSoup

url=''

# ya url pa get reguest mara ga 
r=requests.get(url)

# ya page ma sa html text parse kara ga 
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

# ya page ma mojod sara h2 lines print kara ga 
for h2 in soup.find_all('h2'):
    print(h2)
