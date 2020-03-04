# gcs-websources-ingressor
Containerized flask app to fetch web resources on request &amp; store in Google Cloud Storage (GCS)

## Features
1. Get web resources when given an URI
2. Found if GCS bucket already has this resource
3. (If resource is not found, OR it is updated) Upload the fetched resource to GCS bucket

## Usage
Make a POST request to / (root), with JSON format as follows:
```
{
  "uri": "https://example.com/very-important-web-resources"
}
```

## Installation
1. Add your GCP service account JSON key file to the project
2. Edit `.config.example` so that `KeyFile` points to the key file, and `BucketName` points to your GCS bucket.
3. Move `.config.example` to `.config`
4. Build Docker image by running `docker build . --tag={your-tag-goes-here}`



## Run
`docker run -p8080:8080 {your-tag-goes-here}`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
