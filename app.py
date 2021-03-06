import configparser

from flask import Flask, request, jsonify

from fetch import get_content
from storage import GCPStorageAPI
from buffer import byte2buffer

CONFIG_LOCATION = ".config"
app = Flask(__name__)

config = configparser.ConfigParser()
config.read(CONFIG_LOCATION)

key_file = config['DEFAULT']['KeyFile']
bucket_name = config['DEFAULT']['BucketName']
gcs = GCPStorageAPI(bucket_name, key_file)


@app.route('/', methods=["POST"])
def main():
    json_obj = request.get_json()
    url = json_obj['uri']
    response, obj_name = get_content(url)
    response["newEntry"] = False
    if response['fetchSuccess']:
        obj = response[obj_name]
        blob_path = "{}/{}".format(obj_name, obj['content']['sha1sum'])
        blob = gcs.get_blob(blob_path)
        if not blob:
            response["newEntry"] = True
            buffer = byte2buffer(obj['content']['data'])
            content_type = obj['contentType']
            blob_path, public_uri = gcs.upload(buffer, blob_path, content_type=content_type)
        response[obj_name]['content'].pop('data', None)
    return jsonify(response)


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
