import xlwt
from datetime import datetime
from xlrd import open_workbook

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 'Service_id', style0)
ws.write(0, 1, 'Web_Service', style0)
ws.write(0, 2, 'Start_At', style0)
ws.write(0, 3, 'End_By', style0)
ws.write(0, 4, 'Response_Code', style0)
ws.write(0, 5, 'Json', style0)
# ws.write(1, 0, datetime.now(), style1)

wb.save('example.xls')

wr = open_workbook('example.xls')
s = wr.sheet_by_index(0)
print(s.cell(0,0))