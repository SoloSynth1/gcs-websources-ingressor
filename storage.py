from google.cloud import storage
from google.oauth2 import service_account


class GCPStorageAPI:

    def __init__(self, bucket_name, service_account_file):
        self.credentials = service_account.Credentials.from_service_account_file(service_account_file)
        self.client = storage.Client(project=None, credentials=self.credentials)
        self.update_bucket(bucket_name)

    def update_bucket(self, bucket_name):
        self.bucket_name = bucket_name
        self.public_uri = "https://storage.cloud.google.com/{}/".format(self.bucket_name)
        self.bucket = storage.bucket.Bucket(client=self.client, name=self.bucket_name)

    def list_bucket(self):
        response = self.client.list_blobs(self.bucket_name)
        return response

    def upload(self, buffer, blob_name, content_type=None):
        blob = storage.blob.Blob(name=blob_name, bucket=self.bucket)
        blob.upload_from_file(buffer, content_type=content_type, client=self.client)
        return blob_name, self.public_uri + blob_name

    def get_blob(self, blob_path):
        blob = self.bucket.get_blob(blob_path)
        if blob:
            return blob
        else:
            return None
