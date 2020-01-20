import requests


class Response(object):
    main_page = "empty"

    def __init__(self):
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive'
        }
        # self.url = "qweqweq"
        # self.url = "https://httpstat.us/200"
        self.url = "https://httpstat.us/404"
        # self.url = "https://httpstat.us/403"

    def get(self):
        try:
            response = requests.get(url=self.url, headers=self.headers, timeout=1)
            response.raise_for_status()
            if response.status_code == 404:
                self.main_page = "You will see 404 custom page"
        except requests.exceptions.Timeout:
            print('timeout')
            return 'Bad Response'
        except requests.exceptions.HTTPError as e:
            print(e)
            return "Error: " + str(e)
        print(response)
        return response
