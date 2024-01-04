# Tracking HN Bus System

## Steps to Run this Project
<p> 1. Start Zookeeper : <code> zookeeper-server-start config\zookeeper.properties </code> <br>
    2. Start Kafka     : <code> kafka-server-start config\server.properties </code> <br>
    3. Create Topic    : <code> kafka-topics --bootstrap-server localhost:9092 --topic vehicle_tracking --create --partitions 2 --replication-factor 1 </code> <br>
    4. Run both producer code vehicledata1.py and vehicledata2.py <br>
    5. Run consume file app.py <br>
    6. or run only Makefile using (make run)<br>
    7. Open localhost:5001 to see the Tracking Map <br>
    8. run storage.py to storage data to MongoDb <br>
    9. run visualize.py to visualize fuel data from MongoDB <br>
    
