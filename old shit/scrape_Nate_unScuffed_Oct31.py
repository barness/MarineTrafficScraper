import requests
from bs4 import BeautifulSoup
import itertools
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

main_url = 'https://www.marinetraffic.com/'

details_id = "group-ib short-line vertical-offset-5"
position_id = "tabs-last-pos"

ShipList = ['en/ais/details/ships/shipid:3927580/mmsi:367629440/vessel:367629440']
#ShipList=['en/ais/details/ships/shipid:3927670/mmsi:368437000/vessel:368437000'] 
#'en/ais/details/ships/shipid:4013342/mmsi:367441140/vessel:367441140',
#'en/ais/details/ships/shipid:4086128/mmsi:369713000/vessel:369713000',
#'en/ais/details/ships/shipid:3927580/mmsi:367629440/vessel:367629440',
#'en/ais/details/ships/shipid:4015273/mmsi:338299000/vessel:338299000']

def scrapeURL(url):
        
    my_url = main_url + url
    
    response = requests.get(my_url, headers=headers)
    html = response.content
    
    soup = BeautifulSoup(html, 'html.parser')

    listy0 = []
    
    for i in soup.find_all("div", details_id):
        listy0.append(i.text.strip().replace('\n', ""))
    
    for i in soup.find_all(id=position_id):    
        listy1=i.text.strip().replace('\n', "")
       

    ShipData=''
    
    for i in listy0:
        ShipData += i+'\n'
    
    print(ShipData)
    
    start0 = listy1.partition("Vessel's Local Time:")
    starto=start0[0].split()
    processed0=''
    for j in starto:
        if j=="Position":
            processed0+=j
        else:
            processed0+=' '+j
    print(processed0)
    ShipData+=processed0+'\n'
    rest0 = start0[1]+start0[2]

    later0 = rest0.partition("Area:")
    print(later0[0])
    ShipData+=later0[0]+'\n'
    rest1 = later0[1]+later0[2]

    later1 = rest1.partition("Latitude / Longitude:")
    print(later1[0])
    ShipData+=later1[0]+'\n'
    rest2 = later1[1]+later1[2]
    
    later2 = rest2.partition("Status:")
    print(later2[0])
    ShipData+=later2[0]+'\n'
    rest3 = later2[1]+later2[2]

    later3 = rest3.partition("Speed/Course:")
    print(later3[0][:7]+' '+later3[0][7:])
    ShipData+=later3[0][:7]+' '+later3[0][7:]+'\n'
    rest4 = later3[1]+later3[2]
    
    later4 = rest4.partition("Nearby")
    print(later4[0])
    ShipData+= later4[0]+'\n'

    #get IMO from start1[0] string in format "IMO: XXXXXX"
    #IMO=start1[0].split()
    IMOFileName = "helloiamafile"
    #IMOFileName=IMO[1]
    #print(IMOFileName)
    #print("Printing ship data \n\n\n")
    #print(ShipData)
    
    file = open(IMOFileName+'.txt', 'a')
    #lets figure out whats gucci with encoding so we dont have to call .encode() here
    file.write(ShipData.encode('utf-8'))
    file.write('\n\n\n\n')
    file.close()

#ShipList is a list of all unique url's associated with each ship
#Pull data from each ship once every 15 minutes
while True:
    for i in ShipList:
        scrapeURL(i)
    time.sleep(5*60)
        

