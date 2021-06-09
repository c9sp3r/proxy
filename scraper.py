import requests
from bs4 import BeautifulSoup



html = requests.get('https://www.free-proxy-list.net/')
content = BeautifulSoup(html.text, 'html.parser')
table = content.find('table')
rows = table.findAll('tr')

results = ""

for row in rows:
    url = ""
    liste = ""
    i = 0
    if len(row.findAll('td')):
        for data in row.findAll('td'):
            if i==0:
                i=i+1
                url = url + data.text +":"
            elif i==1:
                i=i+1
                url = url + data.text 
                liste+=url 
            else:
                break       
        results+=liste+"\n"

print(results)
f=open("proxy.txt","w")
f.write(str(results))
f.close()

