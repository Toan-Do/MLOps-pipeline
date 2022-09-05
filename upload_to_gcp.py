import glob
import os
from google.cloud import storage

client = storage.Client()


def upload_from_directory(
    directory_path: str, destination_bucket_name: str, destination_blob_name: str
):
    rel_paths = glob.glob(directory_path + "/**", recursive=True)
    bucket = client.get_bucket(destination_bucket_name)
    for local_file in rel_paths:
        remote_path = (
            f'{destination_blob_name}/{"/".join(local_file.split(os.sep)[-1:])}'
        )
        print(remote_path)
        if os.path.isfile(local_file):
            blob = bucket.blob(remote_path)
            blob.upload_from_filename(local_file)


if __name__ == "__main__":
    upload_from_directory(
        "/home/toando/Working/MLOps/My-Capstone-MLOPS/dataset_val",
        "dvtoan7997",
        "dataset_val",
    )
