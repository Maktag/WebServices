from readAll import service_test
import multiprocessing
import time
import requests

# def call_service():
#     se = service_test("https://cerebellum.medocity.com/v2/login")
#     params = {'password': 'qwerty11', 'userName': 'pproddr@yopmail.com'}
#     header = {'app_name': 'Medocity MD'}
#     se.make_request(params,header,'Post')
#     print(se.return_json()['message'])
#     print(se.return_status_code())
#
# def Users(users,loop):
#     tic = time.time()
#     for j in range(loop):
#         for i in range(users):
#             p1 = multiprocessing.Process(target=call_service())
#             p1.start()
#             p1.join()
#         tac = time.time()
#         print("Total time taken by", (j+1)," loop", tac - tic)
#
#
# if __name__ == '__main__':
#     call_service()

params = {'password': 'qwerty11', 'userName': 'pproddr@yopmail.com'}
header = {'app_name': 'Medocity MD'}
request_call = requests.post(url="https://cerebellum.medocity.com/v2/login", data=params, headers=header)
print(request_call.json())