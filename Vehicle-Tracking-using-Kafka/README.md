# Vehicle-Tracking-using-Kafka
Tracking location of a Vehicle using Kafka Streaming and outputting data on browser using leaflet.js

## Video Demo
https://drive.google.com/file/d/1AwjA10MAOraNeU_WmKrJtt-8Gu0cl-Ek/view?usp=sharing

## Steps to Run this Project
<p> 1. Start Zookeeper : <code> zookeeper-server-start config\zookeeper.properties </code> <br>
    2. Start Kafka     : <code> kafka-server-start config\server.properties </code> <br>
    3. Create Topic    : <code> kafka-topics --bootstrap-server localhost:9092 --topic vehicle_tracking --create --partitions 2 --replication-factor 1 </code> <br>
    4. Run both producer code vehicledata1.py and vehicledata2.py <br>
    5. Run consume file app.py <br>
    6. Open localhost:5001 to see the result <br>

## Reference
Code & Dogs --> https://www.youtube.com/channel/UCyXsLg7-8OKM7Cc0dsmntDA
