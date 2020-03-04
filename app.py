from flask import Flask, request, jsonify

from fetch import get_content
from storage import GCPStorageAPI
from buffer import byte2buffer

app = Flask(__name__)
KEY_FILE = "./key/credentials.json"
BUCKET_NAME = "just-another-random-bucket"
gcs = GCPStorageAPI(BUCKET_NAME, KEY_FILE)


@app.route('/', methods=["POST"])
def hello_world():
    json_obj = request.json()
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
            blob_path, public_uri = gcs.upload(buffer, blob_path)
    return jsonify(response)


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
