import re
import scrapy
from bs4 import BeautifulSoup
import requests
import io
i=1
url = 'https://ru.investing.com/commodities/brent-oil-historical-data'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
r = requests.get(url, headers = headers)
with io.open("oil2.html", "w", encoding='utf-8') as output_file:
    output_file.write(str(r.text))
with io.open("oil2.html", encoding='utf-8') as html:
    soup = BeautifulSoup(html, "lxml")
    soup = soup.find("table",{"class":"genTbl closedTbl historicalTbl","id":"curr_table"})
    soup = str(soup.find("tbody"))
    soup = soup.replace("<tr>", "")
    soup = soup.replace("</tr>", "")
    soup = soup.replace("<td class=", "")
    soup = soup.replace("<td data-real-value=", "")
    soup = soup.replace("</td>", "")
    soup = soup.replace('"first left bold noWrap" data-real-value=', "")
    soup = soup.replace("</td>", "")
    soup = soup.replace('"bold greenFont">', "")
    soup = soup.replace('greenFont" data-real-value=', "")
    soup = soup.replace('redFont" data-real-value=', "")
    soup = soup.replace("</td>", "")
    soup = soup.replace('"bold redFont">', "")
    soup = re.sub(r'(?<=\").*?(?=\")', "", soup)
    soup = re.sub(r'(?<=\ ).*?(?=\%)', "", soup)
    soup = soup.replace("%", "")
    soup = soup.replace('"">', "")
    soup = soup.replace('<tbody>', "")
    soup = soup.replace('</tbody>', "")
    soup = soup.replace("\n\n", "")
    soup = soup.replace(" ", "")
    soup = soup.replace(",", ".")
    soup = re.split("\n",soup)
del soup[2::6]
del soup[2::5]
del soup[2::4]
del soup[21::]
while i != len(soup)+1:
    soup[i] = str(float(soup[i])*100)
    soup[i] = soup[i].replace(".", "")
    i+=3

outstr = ""
iterator = 0
for word in soup:
    outstr += word + ";"
    iterator += 1
    if iterator % 3 == 0:
        outstr += "\n"
#soup = ';'.join(soup)
f = open('raw_data.csv', 'w')
f.write(outstr)
f.close()
