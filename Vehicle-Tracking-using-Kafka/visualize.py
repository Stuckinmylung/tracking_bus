import matplotlib.pyplot as plt
import pymongo
import datetime
import time

# Connect to MongoDB
# make sure that you already have MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["BigData_Project"]  
collection = database["bus_data"]

plt.ion()  
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-')  
# Cho busline_id : 00001
busline_query = "00001"

while True:
    cursor = collection.find({"busline": busline_query}).sort('_id', pymongo.DESCENDING).limit(5)
    
    timestamps = []
    fuel_values = []

    for document in cursor:
        timestamp = datetime.datetime.strptime(document['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        timestamps.append(timestamp)
        fuel_values.append(document['fuel'])
    timestamps.reverse() 
    fuel_values.reverse()

    line.set_xdata(timestamps)
    line.set_ydata(fuel_values)

    ax.relim()
    ax.autoscale_view(True, True, True)
    fig.canvas.draw()
    fig.canvas.flush_events()

    time.sleep(2)  # Refresh every 2s
