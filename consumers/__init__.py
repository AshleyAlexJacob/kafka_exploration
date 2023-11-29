import datetime
from kafka import KafkaConsumer

topic = "news"

consumer = KafkaConsumer(
    topic, 
    bootstrap_servers=['localhost:9092'])

def get_video_stream():
    """
    Here is where we recieve streamed images from the Kafka Server and convert 
    them to a Flask-readable format.
    """
    for msg in consumer:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + msg.value + b'\r\n\r\n')