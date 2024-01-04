import confluent_kafka
import pymongo
import json

# Initialize Kafka consumer
consumer = confluent_kafka.Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id" : "unit"
})

# Initialize MongoDB collection
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["BigData_Project"]
collection = database.get_collection("bus_data")

# Function to process Kafka records
def handle_record(record):
    try:
        # Parse the record value
        value = json.loads(record.value())

        # Extract necessary fields (if required)
        data_to_store = {
            "busline": value.get("busline"),
            "key": value.get("key"),
            "timestamp": value.get("timestamp"),
            "coordinates": {
                "latitude": value.get("latitude"),
                "longitude": value.get("longitude")
            },
            "fuel": value.get("fuel")
        }

        # Store the processed data into MongoDB
        collection.insert_one(data_to_store)
    except json.JSONDecodeError:
        print("Error decoding JSON from Kafka record")

# Subscribe to Kafka topic
consumer.subscribe(["vehicle_tracking"])


# Loop continuously to listen for records from Kafka topic
while True:
    # Read a record from Kafka
    record = consumer.poll(0)  # Poll for 1 second

    # If a new record is available, process it
    if record is not None and not record.error():
        handle_record(record)
    # elif record.error():
    #     print(f"Error: {record.error()}")


# Uncomment to drop the collection if needed

