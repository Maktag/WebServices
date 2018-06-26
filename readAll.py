import requests


class service_test:

    request_url = None
    request_type = None
    request_json = None

    def __init__(self, req_url):
        self.request_url = req_url

    def make_request(self, req_data, service_type):
        """Options are 'Post', 'Get', 'Put' and 'Options' """
        if service_type == 'Post':
            self.request_json = requests.post(url=self.request_url, data=req_data)
        elif service_type == 'Get':
            self.request_json = requests.get(url=self.request_url, data=req_data)
        elif service_type == 'Put':
            self.request_json = requests.put(url=self.request_url, data=req_data)
        elif service_type == 'Options':
            self.request_json = requests.options(url=self.request_url, data=req_data)

    def return_json(self):
        data = self.request_json.json()
        return data