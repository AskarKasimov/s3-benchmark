import time


def get_time() -> float:
    return time.time()


def show_content(conn, bucket_name):
    bucket = conn.get_bucket(bucket_name)
    print(bucket.name, ":")
    for key in bucket.list():
        print("{name}\t{size}\t{modified}".format(
            name=key.name,
            size=key.size,
            modified=key.last_modified,
        ))
        bucket.delete_key(key.name)


def create_bucket(conn, bucket_name):
    try:
        bucket = conn.get_bucket(bucket_name)
        for key in bucket:
            bucket.delete_key(key.name)
        conn.delete_bucket(bucket_name)
    except:
        pass
    return conn.create_bucket(bucket_name)


def upload(bucket, name, size):
    key = bucket.new_key(str(name))
    key.set_contents_from_string((b"A" * size).decode())
