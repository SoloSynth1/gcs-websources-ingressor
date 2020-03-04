import urllib3
import hashlib


def get_content(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    if r.status < 400:
        content_hash = hashlib.sha1(r.data).hexdigest()
        uri_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()
        fetched = {
            uri_hash: {
                "uri": url,
                "content": {
                    "data": r.data,
                    "contentsha1sum": content_hash,
                },
            }

        }
        return fetched
    else:
        return None


if __name__ == "__main__":
    print(get_content("https://www.chp.gov.hk/files/pdf/building_list_chi.pdf"))