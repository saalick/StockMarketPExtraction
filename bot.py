import requests
from bs4 import BeautifulSoup
import emoji
import time
def oil():
 urls = ["https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF","https://finance.yahoo.com/quote/%5EGDAXI?p=%5EGDAXI","https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch","https://finance.yahoo.com/quote/CL=F?p=CL=F&.tsrc=fin-srch","https://finance.yahoo.com/quote/%5EDJI?p=^DJI&.tsrc=fin-srch","https://finance.yahoo.com/quote/%5ERUT?p=^RUT&.tsrc=fin-srch","https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch","https://finance.yahoo.com/quote/%5EN225?p=^N225&.tsrc=fin-srch","https://finance.yahoo.com/quote/%5EHSI?p=^HSI&.tsrc=fin-srch"]
 for url in urls:
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  price = soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
  shortname = soup.find("h1",class_="D(ib) Fz(18px)").text
  if 'Gold' in shortname:
      shortname = "Gold in USD"
  elif 'Oil' in shortname:
      shortname = "Brent Cruide Oil in USD"
  elif 'Dow' in shortname:
      shortname = "Dow Jones in USD"
  elif 'Russell' in shortname:
      shortname = "Russell 2000 in USD"
  elif 'NASDAQ' in shortname:
      shortname= "Nasdaq in USD"
  elif 'Nikkei' in shortname:
      shortname = "Nikkei in JPY"
  elif 'DAX' in shortname:
      shortname = "DAX in EUR"
  elif 'Bitcoin' in shortname:
      shortname = "Bitcoin in USD"
  elif 'HANG' in shortname:
     shortname = "Hang Seng in HKD"
  try:
   diff = soup.find("span",class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)").text
  except:
   diff = soup.find("span",class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)").text
  if diff[0]=="-":
    value = shortname + " || current @"+price+" || \U0001F534 dropped: " + diff
    print(value)
    send='https://api.telegram.org/bot' + "2019412223:AAHQls_geeAZPJoGIRxaIwxmpqhbVtCBCGU" + '/sendMessage?chat_id=' + '-1001528245619' + '&parse_mode=Markdown&text=' + value
    requests.get(send)
  elif diff[0]=="+":
    value = shortname + " || current @"+price+" || \U0001F7E2 surged: " + diff
    send='https://api.telegram.org/bot' + "2019412223:AAHQls_geeAZPJoGIRxaIwxmpqhbVtCBCGU" + '/sendMessage?chat_id=' + '-1001528245619' + '&parse_mode=Markdown&text=' + value
    requests.get(send)
#______________________________________________________________________________________________________________________#
def putcall():
 url = "https://www.cboe.com/us/options/market_statistics/#current-stats"
 r = requests.get(url)
 soup = BeautifulSoup(r.content, 'html.parser')
 paras = soup.find("table", class_="data-table")
 newparas = paras.find_all("td")
 value = newparas[-1]
 value = "Aktuelles PUT/CALL Ratio ist "+value.text
 send='https://api.telegram.org/bot' + "2019412223:AAHQls_geeAZPJoGIRxaIwxmpqhbVtCBCGU" + '/sendMessage?chat_id=' + '-1001528245619' + '&parse_mode=Markdown&text=' + value
 requests.get(send)
#_______________________________________________________________________________________________________________________#
def feargreed():
 url = "https://www.tickertape.in/market-mood-index"
 r = requests.get(url)
 soup = BeautifulSoup(r.content, 'html.parser')
 paras = soup.find("span", class_="number").text
 value = "The greed Fear Index right now is "+paras
 send='https://api.telegram.org/bot' + "2019412223:AAHQls_geeAZPJoGIRxaIwxmpqhbVtCBCGU" + '/sendMessage?chat_id=' + '@iamgrwp' + '&parse_mode=Markdown&text=' + value
 requests.get(send)
#_______________________________________________________________________________________________________________________#
def vixindex():
 url = "https://www.marketwatch.com/investing/index/vix"
 r = requests.get(url)
 soup = BeautifulSoup(r.content, 'html.parser')
 paras = soup.find("h2", class_="intraday__price")
 paras = paras.text
 paras = paras.strip()
 value = "Aktueller VIX Index steht bei "+paras
 send='https://api.telegram.org/bot' + "2019412223:AAHQls_geeAZPJoGIRxaIwxmpqhbVtCBCGU" + '/sendMessage?chat_id=' + '-1001528245619' + '&parse_mode=Markdown&text=' + value
 requests.get(send)
#______________________________________________________________________________________________________________________#
while(True):
 time.sleep(600)
 time.sleep(14400)
 putcall()
 vixindex()
 oil()
 #here ou can customize the time
 time.sleep(61200)
 putcall()
 vixindex()
 oil()
 #here you can customixe it again
 time.sleep(10800)

