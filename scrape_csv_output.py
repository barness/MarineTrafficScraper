import requests
from bs4 import BeautifulSoup
import itertools
import time
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

main_url = 'https://www.marinetraffic.com/'

details_id = "vessel_details_general"
position_id = "tabs-last-pos"

is_man_hot = False

ShipList=['en/ais/details/ships/shipid:3927670/mmsi:368437000/vessel:368437000', 
'en/ais/details/ships/shipid:4013342/mmsi:367441140/vessel:367441140',
'en/ais/details/ships/shipid:4086128/mmsi:369713000/vessel:369713000',
'en/ais/details/ships/shipid:3927580/mmsi:367629440/vessel:367629440',
'en/ais/details/ships/shipid:4015273/mmsi:338299000/vessel:338299000',
'en/ais/details/ships/shipid:3918296/mmsi:338221954/vessel:338221954',
'en/ais/details/ships/shipid:4041056/mmsi:367033990/vessel:367033990',
'en/ais/details/ships/shipid:5505511/mmsi:368030070/vessel:368030070',
'en/ais/details/ships/shipid:3508404/mmsi:367543000/vessel:367543000',
'en/ais/details/ships/shipid:3998780/mmsi:368347000/vessel:368347000',
'en/ais/details/ships/shipid:3932639/mmsi:367186270/vessel:367186270',
'en/ais/details/ships/shipid:274750/mmsi:367042740/vessel:367042740',
'en/ais/details/ships/shipid:3929484/mmsi:367575750/vessel:367575750',
'en/ais/details/ships/shipid:4216421/mmsi:366964020/vessel:366964020']

def scrapeURL(url):
        
    my_url = main_url + url
    
    response = requests.get(my_url, headers=headers)
    html = response.content
    
    soup = BeautifulSoup(html, 'html.parser')

    for i in soup.find_all(attrs={"class": "bg-info bg-light padding-10 radius-4 text-left"}):
        listy0=i.text.strip().replace('\n', "")

    for i in soup.find_all(id=position_id):    
        listy1=i.text.strip().replace('\n', "")
       

    ShipData=''
    ship_dictionary={}
    
    if ("Vessel's Local Time:") in listy1:
        start0 = listy1.partition("Vessel's Local Time:")
    else:
        start0 = listy1.partition("Vessel's Time Zone:")
        
    starto=start0[0].split()
    processed0=''
    
    for j in starto:
        if j=="Position":
            processed0+=j
        else:
            processed0+=' '+j
    print(processed0)
    ShipData+=processed0+'\n'
    
    ship_dictionary["Position Received"]=processed0.replace("Position Received: ",'')
    rest0 = start0[1]+start0[2]

    later0 = rest0.partition("Area:")
    print(later0[0])
    ShipData+=later0[0]+'\n'

    if ("Vessel's Local Time:") in listy1:
        ship_dictionary["Vessel's Local Time"]=later0[0].replace("Vessel's Local Time: ",'')
    else:
        ship_dictionary["Vessel's Local Time"]=later0[0].replace("Vessel's Time Zone: ",'')
    rest1 = later0[1]+later0[2]

    later1 = rest1.partition("Latitude / Longitude:")
    print(later1[0])
    ShipData+=later1[0]+'\n'
    
    ship_dictionary["Area"]=later1[0].replace("Area: ",'')    
    rest2 = later1[1]+later1[2]
    
    later2 = rest2.partition("Status")
    print(later2[0])
    ShipData+=later2[0]+'\n'

    ship_dictionary["Latitude / Longitude"]=later2[0].replace("Latitude / Longitude: ",'')
    rest3 = later2[1]+later2[2]

    later3 = rest3.partition("Speed/Course")
    print(later3[0][:7]+' '+later3[0][7:])
    ShipData+=later3[0][:7]+' '+later3[0][7:]+'\n'

    ship_dictionary["Status"]=later3[0].replace("Status:",'')
    rest4 = later3[1]+later3[2]

    if "AIS Source:" not in rest4:
        rest5=rest4
    else:
        later4 = rest4.partition("AIS Source:")
        print(later4[0])
        ShipData+=later4[0]+'\n'

        ship_dictionary["Speed/Course"]=later4[0].replace("Speed/Course: ",'')
        rest5 = later4[1]+later4[2]

    later5 = rest5.partition("Nearby Vessels")
    print(later5[0])
    ShipData+=later5[0]+'\n'
    if "AIS Source:" not in rest4:
        ship_dictionary["Speed/Course"]=later4[0].replace("Speed/Course: ",'')
    else:
        ais_source=later5[0].replace("AIS Source: ",'').split()
        ais_data=''
        for i in ais_source:
            ais_data+=i+' '
        ship_dictionary["AIS Source"]=ais_data
    rest6 = later5[1]+later5[2]

    ####
    ####
    ####
    ####
    
    start2 = listy0.partition("MMSI:")
    rest0 = start2[1]+start2[2]
    
    start1 = rest0.partition("Call Sign:")
    print(start1[0])
    ShipData+=start1[0]+'\n'
    
    ship_dictionary["MMSI"]=start1[0].replace("MMSI: ",'')
    rest0 = start1[1]+start1[2]
    
    later0 = rest0.partition("Flag:")
    print(later0[0])
    ShipData+=later0[0]+'\n'
    
    ship_dictionary["Call Sign"]=later0[0].replace("Call Sign: ",'')
    rest1 = later0[1]+later0[2]
    
    later1 = rest1.partition("AIS Vessel Type:")
    print(later1[0])
    ShipData+=later1[0]+'\n'

    ship_dictionary["Flag"]=later1[0].replace("Flag: ",'')
    rest2 = later1[1]+later1[2]
    
    later2 = rest2.partition("Gross Tonnage:")
    print(later2[0])
    ShipData+=later2[0]+'\n'
    
    ship_dictionary["AIS Vessel Type"]=later2[0].replace("AIS Vessel Type: ",'')
    rest3 = later2[1]+later2[2]
    
    later3 = rest3.partition("Deadweight:")
    print(later3[0])
    ShipData+=later3[0]+'\n'

    ship_dictionary["Gross Tonnage"]=later3[0].replace("Gross Tonnage: ",'')
    rest4 = later3[1]+later3[2]
    
    later4 = rest4.partition("Length Overall                    x Breadth Extreme:")
    print(later4[0].replace('\t',''))
    ShipData+=later4[0]+'\n'

    ship_dictionary["Deadweight"]=later4[0].replace("Deadweight: ",'')
    rest5 = "Length Overall x Breadth Extreme:"+later4[2]
    
    later5 = rest5.partition("Year Built:")
    print(later5[0])
    ShipData+=later5[0]+'\n'

    ship_dictionary["Length Overall x Breadth Extreme"]=later5[0].replace("Length Overall x Breadth Extreme: ",'')
    rest6 = later5[1]+later5[2]
    
    later6 = rest6.partition("Status:")
    print(later6[0])
    ShipData+=later6[0]+'\n'
    ship_dictionary["Year Built"]=later1[0].replace("Year Built: ",'')
    rest7 = later6[1]+later6[2]

    print('\n\n')

    #get MMSI from start1[0] string in format "MMSI: XXXXXX"
    MMSI=start1[0].split()
    MMSIFileName=MMSI[1]

    file = open(MMSIFileName+'.csv', 'a')
    with file:

        fields = ["Position Received", "Vessel's Local Time", "Area", "Latitude / Longitude", "Speed/Course",
                  "AIS Source","MMSI", "Call Sign", "Flag", "AIS Vessel Type", "Gross Tonnage", "Deadweight", "Length Overall x Breadth Extreme", "Year Built", "Status"]
        writer = csv.DictWriter(file, fieldnames=fields)
        
        #run this code to create csv files with correct headers:
        #writer.writeheader()

        writer.writerow(ship_dictionary)

#ShipList is a list of all unique url's associated with each ship
#Pull data from each ship once every 5 minutes
while not is_man_hot:
    for ship in ShipList:
        try:
            scrapeURL(ship)
        #exception handling for failed web requests
        except UnboundLocalError as e:
            print("Uh oh, an error: ", e)
            continue
    print("finna catch a quick fade")
    time.sleep(5*60)
