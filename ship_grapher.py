import turtle


#takes in a list of ship MMSI's and outputs a graph of the ships movement
def display_ship_movement(ship_list):
    t=turtle.Pen()
    t.up()
    lat_start=None
    long_start=None
    color_list=["red", "yellow", "blue", "green", "black"]
    color_index=0
    for i in ship_list:
        t.pencolor(color_list[color_index])
        file_object=open(str(i)+'.txt','r')
        file_object=file_object.read()
        processed_file=file_object.split('Position Received:')
        for data_point in processed_file:
            if ('Latitude / Longitude:') in data_point:
                partition1=data_point.partition('Latitude / Longitude:')
                partition2=partition1[2].partition('Status:')
                latitude_longitude=partition2[0]
                lat_long_partition=latitude_longitude.partition('/')
                latitude=float(lat_long_partition[0].replace('°', ''))
                longitude=float(lat_long_partition[2].replace('°', ''))
                if lat_start==None:
                    lat_start=latitude
                if long_start==None:
                    long_start=longitude
                t.goto((latitude/lat_start)**(30)*300-300, (longitude/long_start)**(30)*300-300)
                t.down()
        t.up()
        color_index+=1
ship_list=[367629440, 338299000, 367441140, 368437000, 369713000]
#ship_list=[338299000]


display_ship_movement(ship_list)
