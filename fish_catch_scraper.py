import requests
from bs4 import BeautifulSoup
import itertools
import time
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

main_url = 'http://www.976-tuna.com/'

details_id = "vessel_details_general"
position_id = "tabs-last-pos"

##ShipList=['en/ais/details/ships/shipid:3927670/mmsi:368437000/vessel:368437000']
ShipList=['e107_plugins/landing/landing2.php?landingmonth.2']

def scrapeURL(url):
        
    my_url = main_url + url
    
    response = requests.get(my_url, headers=headers)
    html = response.content
    
    soup = BeautifulSoup(html, 'html.parser')

    #info_tag = "group-ib medium-gap line-120 vertical-offset-10"
    #for i in soup.find_all('li', info_tag):
    listy=[]
    for i in soup.find_all(find_tables):
        listy.append(i)
        #listy0=i.text.strip().replace('\n', "")

    #print('\n\n\n\n')

    ShipData=''
    ship_dictionary={}

    print(listy)
    ship_dictionary["ship_name"]=listy

    print('\n\n')

    #get MMSI from start1[0] string in format "MMSI: XXXXXX"
    MMSIFileName="we_did_some_work"

    file = open(MMSIFileName+'.csv', 'a')
    with file:
        fields = ["ship_name", "date", "time", "duration", "anglers", "caught"]
        writer = csv.DictWriter(file, fieldnames=fields)
##      run this code to create csv files with correct headers:
        writer.writeheader()

        writer.writerow(ship_dictionary)
##    file = open(MMSIFileName+'.csv', 'w')
##    file.write(ShipData)
##    file.write('\n\n\n\n')
##    file.close()
def find_tables(tag):
	print(<table style="width:100%"> in tag)
	return <table style="width:100%"> in tag

#ShipList is a list of all unique url's associated with each ship
#Pull data from each ship once every 5 minutes
#program_counter = 0
#while True:
    #if program_counter >= 1000:
       #break
for i in ShipList:
    scrapeURL(i)
	#print(program_counter)
	#program_counter += 1
#time.sleep(24*60*60)
