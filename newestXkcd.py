import re
import urllib


def _get_latest_source():
    try:
        response = urllib.request.urlopen("https://xkcd.com")
        return response.read()
    except urllib.error.URLError:
        return None

def latest_comic_num():
    pattern = \
        r"Permanent link to this comic: https?://xkcd\.com/(?P<num>\d+)/"
    latest_source = _get_latest_source()
    if latest_source is not None:
        permalink = re.search(pattern, str(latest_source))
        return int(permalink.group("num"))
    return None #No latest source, likely internet problems
