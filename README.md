# Tracking HN Bus System

## Steps to Run this Project

1. **Start Zookeeper**:
    ```sh
    zookeeper-server-start config/zookeeper.properties
    ```
2. **Start Kafka**:
    ```sh
    kafka-server-start config/server.properties
    ```
3. **Create Topic**:
    ```sh
    kafka-topics --bootstrap-server localhost:9092 --topic vehicle_tracking --create --partitions 2 --replication-factor 1
    ```
4. **Run Producer Code**:
    - Execute both `vehicledata1.py` and `vehicledata2.py`.
    ```sh
    python vehicledata1.py
    python vehicledata2.py
    ```
5. **Run Consumer Code**:
    - Execute the consumer file `app.py`.
    ```sh
    python app.py
    ```
6. **Alternatively, Use Makefile**:
    - Run the project using Makefile.
    ```sh
    make run
    ```
7. **Open Tracking Map**:
    - Open your web browser and navigate to `localhost:5001` to see the Tracking Map.
8. **Store Data to MongoDB**:
    - Run the storage script `storage.py`.
    ```sh
    python storage.py
    ```
9. **Visualize Fuel Data**:
    - Run the visualization script `visualize.py` to visualize fuel data from MongoDB.
    ```sh
    python visualize.py
    ```


    
