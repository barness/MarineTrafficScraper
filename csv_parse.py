import csv

def parse(csv_file, txt_file):
    with open(csv_file, "a") as outfile:
        with open(txt_file, "r+") as infile:
            for line in infile:
                val = line.partition(":")[2]
                outfile.write(val)
#parse("csv_file.csv", "test.txt")

params = ["Position Received", "Vessel's Time Zone", "Area",
"Latitude / Longitude", "Status", "Speed/Course",
"AIS Source", "MMSI", "Call Sign", "Flag","AIS Vessel Type",
"Deadweight", "Length Overall x Breadth Extreme", "Year Built"]

def make_csv(paramList, fileName, inFileName):
    with open(inFileName, "r") as infile:
        with open(fileName, "wb") as outfile:
            for i in paramList:
                outfile.write(i+" ,")
            writer = csv.writer(outfile, delimiter=" ")
            for line in infile:
                writer.writerow(line)
make_csv(params, "testCSV.csv", "test.txt")