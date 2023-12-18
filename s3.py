import boto
import boto.s3.connection
import threading
import os
from funcs import *

HOST = os.getenv("HOST")
BUCKET_NAME = os.getenv("BUCKET_NAME")
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv(
    "SECRET_KEY")
OBJECTS_COUNT = int(os.getenv("OBJECTS_COUNT"))
OBJECT_SIZE = int(os.getenv("OBJECT_SIZE"))

conn = boto.connect_s3(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    host=HOST,
    calling_format=boto.s3.connection.OrdinaryCallingFormat(),
)

bucket = create_bucket(conn, BUCKET_NAME)

start_time = get_time()

threads = []
for i in range(0, OBJECTS_COUNT):
    thread = threading.Thread(target=upload, args=(bucket, i, OBJECT_SIZE))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()

end_time = get_time()

show_content(conn, BUCKET_NAME)

result = end_time - start_time

print(f"{result} — total time to upload {OBJECTS_COUNT} {OBJECT_SIZE} (bytes) objects (using {OBJECTS_COUNT} threads)")
print(f"{1 / result / 30} — seconds per 1 object")
