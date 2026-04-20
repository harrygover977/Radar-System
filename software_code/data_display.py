import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from read_data import read_data
import threading

fig, ax = plt.subplots()

def update(frame):
    try:
        df = pd.read_csv("data.csv")
        
        clean_data = df[1:]
        ax.clear()
        ax.plot(clean_data["position"], clean_data["distance"])
        ax.set_xlabel('position')
        ax.set_ylabel('distance')
        
    except Exception as e:
        print(f"Error: {e}")
        
    threading.Thread(target=read_data, daemon=True).start()

ani = FuncAnimation(fig, update, interval=180)
plt.show()
