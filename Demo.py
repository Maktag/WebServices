# from readAll import service_test
#
# se = service_test("https://cerebellum.medocity.com/v2/login")
# PARAMS = {'password':'qwerty11','userName':'pproddr@yopmail.com'}
# se.make_request(PARAMS)
# print(se.return_json()['message'])

import multiprocessing
import timeit

def PrintName():
    pass
    # print('Mayank Tyagi')

p1 = multiprocessing.Process(target=PrintName)
p2 = multiprocessing.Process(target=PrintName)

tic = timeit.default_timer()
print(tic)
p1.start()
tac = timeit.default_timer()
print(tac)
p2.start()
too = timeit.default_timer()
print(too)

p1.join()
p2.join()

print(tac-tic)
print(too-tac)