#-*- coding: utf-8 -*-
import csv
#import pandas

    
params = ["Position Received", "Vessel's Time Zone", "Area",
"Latitude / Longitude", "Status", "Speed/Course",
"AIS Source", "MMSI", "Call Sign", "Flag","AIS Vessel Type",
"Deadweight", "Length Overall x Breadth Extreme", "Year Built"]

samsdumbstring = u'2018-11-03 18:23 UTC, UTC -7, USWC - US West Coast, 32.72333° / -117.2271°, Stopped, 0.0kn / -, 708 ShipTrackingAIS.blogspot.com, 368437000, WDG6294, USA [US], Passenger, - , - , 23.4m × 6.8m, -' 


def fx():
    with open("samscsvmfile.csv", 'a', newline='') as outfile:
        for i in params:
            outfile.write(i+", ")
            writer = csv.writer(outfile, delimiter=",")
            for line in samsdumbstring:
                writer.writerow(line.encode('utf-8'))
fx()




def parse(csv_file, txt_file):
    with open(csv_file, "a") as outfile:
        with open(txt_file, "r+") as infile:
            for line in infile:
                val = line.partition(":")[2]
                outfile.write(val)
#parse("csv_file.csv", "test.txt")


def make_csv(paramList, fileName, inFileName):
    with open(inFileName, "r") as infile:
        with open(fileName, "wb") as outfile:
            for i in paramList:
                outfile.write(i+" ,")
            writer = csv.writer(outfile, delimiter=" ")
            for line in infile:
                writer.writerow(line)
#make_csv(params, "testCSV.csv", "test.txt")