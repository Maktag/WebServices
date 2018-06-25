import requests


class service_test:

    request_url = None
    request_type = None
    request_json = None

    def __init__(self, req_url):
        self.request_url = req_url

    def make_request(self, req_data, service_type):
        # URL = "https://cerebellum.medocity.com/v2/login"
        if service_type == 'POST':
            self.request_json = requests.post(url=self.request_url, data=req_data)
        elif service_type == 'Get':
            self.request_json = requests.get(url=self.request_url, data=req_data)
        elif service_type == 'PUT':
            self.request_json = requests.put(url=self.request_url, data=req_data)
        elif service_type == 'Get':
            self.request_json = requests.options(url=self.request_url, data=req_data)




    def return_json(self):
        data = self.request_json.json()
        return data