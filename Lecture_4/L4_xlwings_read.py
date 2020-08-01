import xlwings as xw

app = xw.App(visible=True, add_book=False)
wb = app.books.open('社会实践报名表.xlsx')
sht = wb.sheets["sheet1"]


rows = sht.range('A' + str(wb.sheets[0].cells.last_cell.row)).end('up').row
countries = sht["A2:A"+str(rows)].value
description = sht["B2:B"+str(rows)].value
department = sht["C2:C"+str(rows)].value
number = sht["D2:D"+str(rows)].value
plan = sht["e2:e"+str(rows)].value


wb.save()
wb.close()
app.quit()


