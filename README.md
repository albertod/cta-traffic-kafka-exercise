# cta-traffic-kafka-exercise

Running and Testing

NOTE: You must allocate at least 4gb RAM to your Docker-Compose environment to run locally.

To run the simulation, you must first start up the Kafka ecosystem on your machine utilizing Docker-Compose.

%> docker-compose up

Docker-Compose will take 3-5 minutes to start, depending on your hardware. Please be patient and wait for the Docker-Compose logs to slow down or stop before beginning the simulation.

Once Docker-Compose is ready, the following services will be available on your local machine:

Note that to access these services from your own machine, you will always use the Host URL column.

When configuring services that run within Docker-Compose, like Kafka Connect, you must use the Docker URL. When you configure the JDBC Source Kafka Connector, for example, you will want to use the value from the Docker URL column.

Running the Simulation
There are two pieces to the simulation, the producer and consumer. As you develop each piece of the code, it is recommended that you only run one piece of the project at a time.

cd producers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python simulation.py

Once the simulation is running, you may hit Ctrl+C at any time to exit.

To run the Faust Stream Processing Application:

cd consumers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
faust -A faust_stream worker -l info

To run the KSQL Creation Script:

cd consumers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python ksql.py

To run the consumer:

cd consumers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python server.py

Once the server is running, you may hit Ctrl+C at any time to exit.
