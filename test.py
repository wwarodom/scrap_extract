from bs4 import BeautifulSoup
from bs4.element import Comment
#import urllib.request
import requests
import csv



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
    
    f = open("output.txt", "w")
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

html = requests.request("GET", url, headers=headers)
html.encoding = 'utf-8'
print(text_from_html(html.content).encode("utf-8"))

#writer.writerow(['Erica Meyers', 'IT', 'March'])