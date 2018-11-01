import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
helpful_link = 'en/ais/details/ships/shipid:442329/vessel:NORTHWESTERN'
helpful_link1 = 'en/ais/details/ships/shipid:370651/mmsi:309933000/imo:9053878/vessel:CARNIVAL_IMAGINATION/_:2e1cc12ea150ce8d47c1cb5e7db7354d'
helpful_link2 = 'en/ais/details/ships/shipid:5426876/mmsi:232012789/imo:9817626/vessel:ENERGY_TROPHY/_:2e1cc12ea150ce8d47c1cb5e7db7354d'

main_url = 'https://www.marinetraffic.com/'


details_id = "vessel_details_general"
position_id = "tabs-last-pos"

def scrapeURL(url):
        
    my_url = main_url + url
    
    response = requests.get(my_url, headers=headers)
    html = response.content
    
    soup = BeautifulSoup(html, 'html.parser')
    
    listy0, listy1 = [], []

    #info_tag = "group-ib medium-gap line-120 vertical-offset-10"
    #for i in soup.find_all('li', info_tag):
    for i in soup.find_all(id=details_id):
        listy0.append(i.text)
    
    #position_tag = "vertical-offset-10 group-ib"
    #for i in soup.find_all('div', position_tag):
    for i in soup.find_all(id=position_id):    
        listy1.append(i.text.strip().replace('\n', ""))
        
    print(listy1)
    """
    for i in listy0:
        
        start = i.partition("Name:")
        print(start[0])
        rest0 = start[1]+start[2]
        
        later0 = rest0.partition("MMSI:")
        print(later0[0])
        rest1 = later0[1]+later0[2]
        
        later1 = rest1.partition("Vessel Type:")
        print(later1[0])
        rest2 = later1[1]+later1[2]
        
        later2 = rest2.partition("Gross Tonnage:")
        print(later2[0])
        rest3 = later2[1]+later2[2]
        
        later3 = rest3.partition("Summer DWT:")
        print(later3[0])
        rest4 = later3[1]+later3[2]
        
        later4 = rest4.partition("Build:")
        print(later4[0])
        rest5 = later4[1]+later4[2]
        
        later5 = rest5.partition("Flag:")
        print(later5[0])
        rest6 = later5[1]+later5[2]
        
        later6 = rest6.partition("Home port:")
        print(later6[0])
        rest7 = later6[1]+later6[2]
        
        print(rest7)
        """

        
        #print(i.partition("Name:")[0])
        #print((i.partition("Name:")[2]).partition("Vessel Type:")[0])
        #print("x")
        #print(i.partition("IMO:")[1])
        #print("x")
        #print(i.partition("IMO:")[2])
        #print(i.partition("Vessel Type:")[0])
        #print(i.partition("Gross Tonnage:")[0])
        #print(i.partition("Build:")[0])
        #print(i.partition("Flag:")[0])
    

scrapeURL(helpful_link2)
