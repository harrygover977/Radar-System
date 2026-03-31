import serial 
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    # initialise the port where the data is being read from 
    ser = serial.Serial('COM6', 9600)

    # refresh the csv file each time the program runs 
    pd.DataFrame(columns =['position', 'distance']).to_csv('data.csv', index=False)

    for i in range(182):
        try:
        # read each line from the serial port
            line = ser.readline()
            # decode each line read 
            decoded = line.decode('utf-8').strip()
            # split the header values into a list
            if i == 0:
                continue
            # split the data points into lists
            else:
                values = [float(x) for x in decoded.split()]
            print(values)
            # create a new row for each data point 
            new_row = pd.DataFrame([{
                'position': values[0],
                'distance': values[1]
            }])
            
            #append the row to the csv file in real time 
            new_row.to_csv('data.csv',
                        mode ='a',
                        header=i == 0,
                        index=False)
        except:
            print("Error reading data point!")

        
        
