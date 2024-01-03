from flask import Flask, render_template, Response
from pykafka import KafkaClient
import json
from datetime import datetime
import math

def get_kafka_client():
    return KafkaClient(hosts='localhost:9092')

app = Flask(__name__)

# Assuming you have a global variable to store previous data
previous_data = {
    'timestamp': None,
    'latitude': None,
    'longitude': None
}

# Function to calculate distance (Haversine formula)
def calculate_distance(lat1, lon1, lat2, lon2):
    # Implementation of Haversine formula...
    # ...
     # Radius of the Earth in km
    R = 6371.0

    # Convert coordinates from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # in kilometers

    # Convert to meters
    return distance * 1000

@app.route('/')
def index():
    return render_template('index.html')

previous_data = {}

@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()

    def events():
        global previous_data

        for message in client.topics[topicname].get_simple_consumer():
            data = json.loads(message.value.decode())

            # Unique vehicle identifier, e.g., busline
            vehicle_id = data.get('busline')

            if vehicle_id not in previous_data:
                previous_data[vehicle_id] = {'timestamp': None, 'latitude': None, 'longitude': None}

            # Calculate velocity
            prev_data = previous_data[vehicle_id]
            if prev_data['timestamp']:
                current_time = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
                previous_time = datetime.strptime(prev_data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
                time_diff = (current_time - previous_time).total_seconds()

                if time_diff > 0:
                    distance = calculate_distance(prev_data['latitude'], prev_data['longitude'],
                                                  data['latitude'], data['longitude'])
                    velocity = distance / time_diff  # m/s
                    data['velocity'] = velocity
                else:
                    data['velocity'] = 0
            else:
                data['velocity'] = 0

            previous_data[vehicle_id] = data

            # Send data including velocity
            yield f'data:{json.dumps(data)}\n\n'

    return Response(events(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, port=5001, use_reloader=False)
