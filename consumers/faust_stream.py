"""Defines trends calculations for stations"""
import logging

import faust


logger = logging.getLogger(__name__)


# Faust will ingest records from Kafka in this format
class Station(faust.Record):
    stop_id: int
    direction_id: str
    stop_name: str
    station_name: str
    station_descriptive_name: str
    station_id: int
    order: int
    red: bool
    blue: bool
    green: bool
        
    def line_color(self):
        if self.red:
            return "red"
        elif self.blue:
            return "blue"
        elif self.green:
            return "green"
        else:
            return "n/a"


# Faust will produce records to Kafka in this format
class TransformedStation(faust.Record):
    station_id: int
    station_name: str
    order: int
    line: str


# TODO: Define a Faust Stream that ingests data from the Kafka Connect stations topic and
#   places it into a new topic with only the necessary information.

app = faust.App("stations-stream", broker="kafka://localhost:9092", store="memory://")
topic = app.topic("updatesstations", value_type=Station)
out_topic = app.topic("org.chicago.cta.stations.table.v1", partitions=1)


table = app.Table(
   "org.chicago.cta.stations.table.v1",
   default=int,
   partitions=1,
   changelog_topic=out_topic,
)


@app.agent(topic)
async def process_station_updates(station_events):
    async for event in station_events:
        table[event.station_id] = TransformedStation(station_id=event.station_id, station_name=event.station_name, order=event.order, line=event.line_color())


if __name__ == "__main__":
    app.main()
