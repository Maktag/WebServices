import csv
from readAll import service_test

with open('Services.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    rows = list(reader)
    for row in range(len(rows)):
        # for col in range(len(rows[0])):
        if row >0:
            # print(rows[row][col])
            method = rows[row][1]
            se = service_test(rows[row][2])
            params = rows[row][3]
            header = rows[row][4]
            print(method)
            print(params)
            print(header)
            se.make_request(params, header, 'Post')
            # se.return_json()
            # print(se.return_status_code())
    # print(rows[1][3])

    # for row in reader:
    #     print(row[1])

csvFile.close()