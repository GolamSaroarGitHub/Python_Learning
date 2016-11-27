import openpyxl



## Get the names of  the sheet of the excel sheet

wb=openpyxl.load_workbook('example.xlsx')
print(wb.get_sheet_names())

#Get the namme of the sheet
sheet=wb.get_sheet_by_name('Sheet1')
print(sheet.title)
print(sheet['A1'].value)