import time
from kafka import KafkaProducer
import cv2
import sys

topic = "news"

def publish_video(video_file):

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    video = cv2.VideoCapture(video_file)
    print('publishing Video')

    while(video.isOpened()):
        success,frame = video.read()

        if not success:
            print('bad Read!')
            break

        ret, buffer = cv2.imencode('.jpg', frame)

        producer.send(topic, buffer.tobytes())

        time.sleep(0.2)

    video.release()
    print('publish complete')


def publish_camera():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    camera = cv2.VideoCapture(0)
    
    try:
        while(True):
            success, frame = camera.read()
            ret, buffer = cv2.imencode('.jpg', frame)

            producer.send(topic, buffer.tobytes())

            time.sleep(0.2)
    except:
        print("\nExiting.")
        sys.exit(1)

    camera.release()

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        video_path = sys.argv[1]
        publish_video(video_path)
    
    else:
        print("Publishing Feed")
        publish_camera()
            
