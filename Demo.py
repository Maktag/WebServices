from readAll import service_test

# se = service_test("https://cerebellum.medocity.com/v2/login")
# PARAMS = {'password':'qwerty11','userName':'pproddr@yopmail.com'}
# se.make_request(PARAMS)
# print(se.return_json()['message'])

import multiprocessing
import time


def call_service():
    se = service_test("https://cerebellum.medocity.com/v2/login")
    params = {'password': 'qwerty11', 'userName': 'pproddr@yopmail.com'}
    se.make_request(params,'Post')
    print(se.return_json()['message'])
    print(se.return_status_code())
def Users(users,loop):
    tic = time.time()
    for j in range(loop):
        for i in range(users):
            p1 = multiprocessing.Process(target=call_service())
            p1.start()
            p1.join()
        tac = time.time()
        print("Total time taken by", (j+1)," loop", tac - tic)


if __name__ == '__main__':
    Users(1,2)