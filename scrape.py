import requests
from BeautifulSoup import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
helpful_link = 'en/ais/details/ships/shipid:442329/vessel:NORTHWESTERN'

def scrapeURL(url):
        
    main_url = 'https://www.marinetraffic.com/'
    my_url = main_url + url
    
    response = requests.get(my_url, headers=headers)
    html = response.content

    soup = BeautifulSoup(html)
    #soup = BeautifulSoup(html, "xml")
    
    #print(soup.title.string)
    print("test")
    
scrapeURL(helpful_link)
