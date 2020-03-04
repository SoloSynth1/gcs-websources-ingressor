import urllib3
import hashlib


def get_content(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    safe_url = url.replace("/", "_")
    uri_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()
    obj_name = "{}_{}".format(safe_url, uri_hash)
    fetched = {
        "fetchSuccess": False,
        obj_name: {
            "uri": url
        }

    }
    try:
        if r.status < 400:
            content_hash = hashlib.sha1(r.data).hexdigest()
            fetched["fetchSuccess"] = True
            fetched[obj_name]["content"] = {
                "sha1sum": content_hash,
                "data": r.data
            }
        return fetched
    except:
        return fetched, obj_name


if __name__ == "__main__":
    print(get_content("https://www.chp.gov.hk/files/pdf/building_list_chi.pdf"))
