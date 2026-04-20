import serial 
import pandas as pd
import matplotlib.pyplot as plt
import threading 

def read_data(data_lock, shared_state):
    # initialise the port where the data is being read from 
    ser = serial.Serial('COM6', 9600)

    # refresh the csv file each time the program runs 
    pd.DataFrame(columns =['position', 'distance']).to_csv('data.csv', index=False)

    i = 0
    clockwise = True
    
    while True:
        try:
        # read each line from the serial port
            line = ser.readline()
            # decode each line read 
            decoded = line.decode('utf-8').strip()
            
            if i < 180 and clockwise:
                i+=1
                if i == 179:
                    clockwise = False
            else:
                i-=1
                if i == 0:
                    clockwise = True
                    with data_lock:
                        shared_state["points"] = []
                
            values = [float(x) for x in decoded.split()]
            
            with data_lock:
                shared_state["angle"] = i
                shared_state["points"].append({
                    "position": i,
                    "distance": values[1]
                })
        except:
            print("Error reading data point!")

        
