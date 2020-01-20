import urllib.error
import urllib.request


# try:
#     from urllib.parse import urljoin
# except ImportError:
#     from urlparse import urljoin

# Third-party imports...
import requests

url = "https://httpstat.us/404"


def start_connection():
    # create connection (will be used in future)
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # HTTP-specific error
        print('HTTPError: {}'.format(e.code))
        if e.code == 404:
            text = "You will see 404 custom page"
            print(text)
            return text
        else:
            raise

    except urllib.error.URLError as e:
        # Not an HTTP-specific error
        return None
        print('URLError: {}'.format(e.reason))
    else:
        # 200
        print(f"You see {url}")
