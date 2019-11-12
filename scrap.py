from bs4 import BeautifulSoup
from bs4.element import Comment
#import urllib.request
import requests
#import csv

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    
    f = open("output.xls", "w")
    for t in visible_texts:
        #print('xx' , t) 	
        f.write(t.encode("utf-8"))
    f.close()
	
	# === write to csv ====
    #with open('data.csv', mode='w') as data_file:
     #   writer = csv.writer(data_file, delimiter='.', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        #writer = csv.writer(data_file)
    #    for t in visible_texts:
     #       print('xx' , t)            
          #  writer.writerow(t.strip().encode("utf-8"))	
     #   writer.writerows((u" ".join(t.strip() for t in visible_texts)).encode("utf-8"))
    return u" ".join(t.strip() for t in visible_texts)

	
# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
url = 'https://www.blognone.com/node/113074' 
urlEng = 'http://plex.coe.psu.ac.th/port/'
url2 = 'https://www.7mscorethai.com/%E0%B8%94%E0%B8%B9%E0%B8%9A%E0%B8%B2%E0%B8%AA%E0%B8%AA%E0%B8%94.html'
url3 = 'https://www.facebook.com/'

html = requests.request("GET", url, headers=headers)
html.encoding = 'utf-8'
text_from_html(html.content).encode("utf-8")
#print(text_from_html(html.content).encode("utf-8")) 