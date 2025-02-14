import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas.core.interchange.dataframe_protocol import DataFrame

url = "https://ticker.finology.in/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

response = requests.get(url, headers=HEADERS)
# print(response)

soup =BeautifulSoup(response.text,"lxml")
# print(soup)
table = soup.find("table", class_ = "table table-sm table-hover screenertable")
# print(table.text)

headers = table.find_all("th")

titles = []

for i in headers:
    title = i.text
    titles.append(title)
# print(titles)

df = pd.DataFrame(columns=titles)
# print(df)

rows = table.find_all("tr")[1:]
# print(rows)

for i in rows[1:]:
    data = i.find_all("td")
    # print(data)
    row = [tr.text.strip("\n") for tr in data]
    # print(row)
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv("India Stock Market.csv")