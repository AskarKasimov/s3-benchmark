# s3-benchmark
## Download

Using Git:

```
git clone https://github.com/AskarKasimov/s3-benchmark
```

Using wget (zip-archive):

```
wget https://github.com/AskarKasimov/s3-benchmark/archive/refs/heads/master.zip
```

## Run
1. Set the following ENV variables (create .env file):
    - `HOST` — url to S3 machine
    - `BUCKET_NAME` — random bucket name for uploading objects
    - `ACCESS_KEY` — access key to S3 machine
    - `SECRET_KEY` — secret key to S3 machine
    - `OBJECTS_COUNT` — number of objects (1 object per 1 thread) to upload
    - `OBJECT_SIZE` — size of 1 object (bytes)
2. Choose between Docker **(recommended)** and usual use:

    - Docker:

       ```
       docker-compose up --build
       ```

    - No Docker:
 
       ```
       pip3 install -r requirements.txt
       python3 s3.py
       ```
