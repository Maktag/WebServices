import requests


class service_test:

    request_url = None
    request_type = None
    request_call = None

    def __init__(self, req_url):
        self.request_url = req_url

    def make_request(self, req_payload, req_header ,service_type):
        """Options are 'Post', 'Get', 'Put' and 'Options' """
        if service_type == 'Post':
            self.request_call = requests.post(url=self.request_url, data=req_payload, headers=req_header)
        elif service_type == 'Get':
            self.request_call = requests.get(url=self.request_url, data=req_payload, headers=req_header)
        elif service_type == 'Put':
            self.request_call = requests.put(url=self.request_url, data=req_payload, headers=req_header)
        elif service_type == 'Options':
            self.request_call = requests.options(url=self.request_url, data=req_payload, headers=req_header)

    def return_json(self):
        data = self.request_call.json()
        return data

    def return_all_keys(self):
        print(self.return_json())

    def return_status_code(self):
        data = self.request_call.status_code
        return data

    def get_value_of_key(self, *keys):
        key_list = []
        # This will give a list of keys
        for key in keys:
            key_list.append(key)

        if len(key_list) == 0:
            return 'Please provide atleast one Key.'
        elif len(key_list) == 1:
            try:
                if isinstance(se.return_json()[key_list[0]], dict):
                    return self.return_json()[key_list[0]]
            except Exception as e:
                print(key_list[0], ' Key does not exist.')
        elif len(key_list) == 2:
            try:
                return self.return_json()[key_list[0]][key_list[1]]
            except Exception as e:
                print([key_list[0]],' or ',[key_list[1]], ' Key does not exist.')
        elif len(key_list) == 3:

            try:
                if isinstance(self.return_json()[key_list[1]],list):
                    return self.return_json()[key_list[0]][key_list[1]][key_list[2]]
                elif isinstance(self.return_json()[key_list[1]],dict):
                    return self.return_json()[key_list[0]][key_list[1]][key_list[2]]
            except Exception as e:
                print([key_list[0]],' or ', [key_list[1]],' or ',[key_list[2]], ' Key does not exist.')
        elif len(key_list) == 4:
            try:
                return self.return_json()[key_list[0]][key_list[1]][key_list[2]][key_list[3]]
            except Exception as e:
                print([key_list[0]],' or ',[key_list[1]],' or ',[key_list[2]],' or ',[key_list[3]], ' Key does not exist.')





# se = service_test("https://cerebellum.medocity.com/v2/login")
# params = {'password': 'qwerty11', 'userName': 'pproddr@yopmail.com'}
# se.make_request(params,'Post')





se = service_test("https://cerebellum.medocity.net/v2/healthtracker")
payload_data = {'date':'2018-6-27'}
header_data={'session':'5b338d9ecdf1ab2c334b7bc1'}
se.make_request(payload_data,header_data,'Get')
print(se.return_json())
print(se.get_value_of_key('message','General',0))















# print(se.get_value_from_Parent_key('message','imageSmall'))














# print(se.return_json().keys())
# dict_keys1 = se.return_json().keys()
# for keys1 in dict_keys1:
#
#     # print(keys1)
#     # print(type(se.return_json()[keys1]))
#
#     if isinstance(se.return_json()[keys1], dict):
#         parent_key = keys1
#         print(se.return_json()[keys1])
#         print(se.return_json()[keys1].keys())
#         dict_keys2 = se.return_json()[keys1]
#         for keys2 in dict_keys2:
#             if isinstance(se.return_json()[keys2], dict):
#                 print(keys2,' is a dict.')