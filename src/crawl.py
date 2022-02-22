import sys
import requests
from bs4 import BeautifulSoup
 
class FmtData:
    def fmt_csv(data):
        return '\'' + data + '\''

fmt_data = FmtData

url = sys.argv
    
response = requests.get(url[1])
response.encoding = response.apparent_encoding
    
bs = BeautifulSoup(response.text, 'html.parser')

# link
link_list = bs.find_all('a')
for link in link_list:
    print(link.get('href'))

# title
title = bs.find('title').contents[0]
csv_title = fmt_data.fmt_csv(title)

# discription
meta_desc = bs.find_all('meta', attrs={'name': 'description'})
desc_cnt = meta_desc[0].get('content')
# 改行コードをなくす
fmt_desc = ' '.join(desc_cnt.splitlines())
csv_desc = fmt_data.fmt_csv(fmt_desc)

# h1
h1 = bs.find('h1').contents[0]
# csv_h1 = fmt_data.fmt_csv(h1)

print(csv_title)
print(csv_desc)
print(h1)