import csv
from readAll import service_test
import json
import time

with open('Services.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    rows = list(reader)
    for row in range(len(rows)):
        if row >0:
            method = rows[row][1]
            se = service_test(rows[row][2])
            params = rows[row][3]
            header = rows[row][4]
            params_j = json.loads(params)
            header_j = json.loads(header)
            start_time = time.time()
            if 'session' in header_j:
                header_j['session'] = rows[1][7]
            se.make_request(params_j, header_j, method)
            time_taken = time.time() - start_time
            # print(se.return_json()['session'])
            # print(se.return_status_code())
            rows[row][5] = se.return_status_code()
            rows[row][6] = str(round(time_taken))+" sec"
            try:
                rows[row][7] = se.return_json()['session']
            except Exception as error_session:
                pass
                # print(error_session)
            my_new_list = open('Services.csv', 'w', newline='')
            csv_writer = csv.writer(my_new_list)
            csv_writer.writerows(rows)
            print(rows[row][0],' service has been verified.')
            my_new_list.close()
csvFile.close()

