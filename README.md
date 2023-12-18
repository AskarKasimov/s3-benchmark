# s3-benchmark
## Run
Set the following ENV variables (create .env file):
- `HOST` — url to S3 machine
- `BUCKET_NAME` — random bucket name for uploading objects
- `ACCESS_KEY` — access key to S3 machine
- `SECRET_KEY` — secret key to S3 machine
- `OBJECTS_COUNT` — number of objects (1 object per 1 thread) to upload
- `OBJECT_SIZE` — size of 1 object (bytes)
