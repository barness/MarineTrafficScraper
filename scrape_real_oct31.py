import requests
from bs4 import BeautifulSoup
import itertools
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

main_url = 'https://www.marinetraffic.com/'

details_id = "vessel_details_general"
position_id = "tabs-last-pos"

##ShipList=['en/ais/details/ships/shipid:3927670/mmsi:368437000/vessel:368437000']
ShipList=['en/ais/details/ships/shipid:3927670/mmsi:368437000/vessel:368437000', 
'en/ais/details/ships/shipid:4013342/mmsi:367441140/vessel:367441140',
'en/ais/details/ships/shipid:4086128/mmsi:369713000/vessel:369713000',
'en/ais/details/ships/shipid:3927580/mmsi:367629440/vessel:367629440',
'en/ais/details/ships/shipid:4015273/mmsi:338299000/vessel:338299000']

def scrapeURL(url):
        
    my_url = main_url + url
    
    response = requests.get(my_url, headers=headers)
    html = response.content
    
    soup = BeautifulSoup(html, 'html.parser')

    #info_tag = "group-ib medium-gap line-120 vertical-offset-10"
    #for i in soup.find_all('li', info_tag):
    for i in soup.find_all(attrs={"class": "bg-info bg-light padding-10 radius-4 text-left"}):
        listy0=i.text.strip().replace('\n', "")
    #position_tag = "vertical-offset-10 group-ib"
    #for i in soup.find_all('div', position_tag):
    for i in soup.find_all(id=position_id):    
        listy1=i.text.strip().replace('\n', "")
       
    #print(listy1)

    #print('\n\n\n\n')

    ShipData=''
    
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
    
    later2 = rest2.partition("Status")
    print(later2[0])
    ShipData+=later2[0]+'\n'
    rest3 = later2[1]+later2[2]

    later3 = rest3.partition("Speed/Course")
    print(later3[0][:7]+' '+later3[0][7:])
    ShipData+=later3[0][:7]+' '+later3[0][7:]+'\n'
    rest4 = later3[1]+later3[2]

    if "AIS Source:" not in rest4:
        rest5=rest4
    else:
        later4 = rest4.partition("AIS Source:")
        print(later4[0])
        ShipData+=later4[0]+'\n'
        rest5 = later4[1]+later4[2]

    later5 = rest5.partition("Nearby Vessels")
    print(later5[0])
    ShipData+=later5[0]+'\n'
    rest6 = later5[1]+later5[2]

    #print(listy1)


    #List0 parsing
    start2 = listy0.partition("MMSI:")
    rest0 = start2[1]+start2[2]
    #rest0.replace('Overall                    x','Overall x')
    
    start1 = rest0.partition("Call Sign:")
    print(start1[0])
    ShipData+=start1[0]+'\n'
    rest0 = start1[1]+start1[2]
    
    later0 = rest0.partition("Flag:")
    print(later0[0])
    ShipData+=later0[0]+'\n'
    rest1 = later0[1]+later0[2]
    
    later1 = rest1.partition("AIS Vessel Type:")
    print(later1[0])
    ShipData+=later1[0]+'\n'
    rest2 = later1[1]+later1[2]
    
    later2 = rest2.partition("Gross Tonnage:")
    print(later2[0])
    ShipData+=later2[0]+'\n'
    rest3 = later2[1]+later2[2]
    
    later3 = rest3.partition("Deadweight:")
    print(later3[0])
    ShipData+=later3[0]+'\n'
    rest4 = later3[1]+later3[2]
    
    later4 = rest4.partition("Length Overall                    x Breadth Extreme:")
    print(later4[0].replace('\t',''))
    ShipData+=later4[0]+'\n'
    rest5 = later4[1]+later4[2]
    
    later5 = rest5.partition("Year Built:")
    print(later5[0])
    ShipData+=later5[0]+'\n'
    rest6 = later5[1]+later5[2]
    
    later6 = rest6.partition("Status:")
    print(later6[0])
    ShipData+=later6[0]+'\n'
    rest7 = later6[1]+later6[2]
          
    #print(rest7)
    #ShipData+=rest7

    print('\n\n')
    

    #get IMO from start1[0] string in format "IMO: XXXXXX"
    IMO=start1[0].split()
    IMOFileName=IMO[1]
    #print(IMOFileName)
    
    file = open(IMOFileName+'.txt', 'a')
    file.write(ShipData.encode('utf-8'))
    file.write('\n\n\n\n')
    file.close()

#ShipList is a list of all unique url's associated with each ship
#Pull data from each ship once every 15 minutes
#program_counter = 0
while True:
    #if program_counter >= 1000:
       #break
    for i in ShipList:
        scrapeURL(i)
	#print(program_counter)
	#program_counter += 1
    time.sleep(5*60)
