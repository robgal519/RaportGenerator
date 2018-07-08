import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell


def generate_excel_sheet_header(workbook, file):
    worksheet = workbook.add_worksheet(file)
    empty_revision = workbook.add_format({'bg_color': 'red'})

    worksheet.write("B1", "Revision")

    worksheet.conditional_format('C1', {'type': 'blanks',
                                        'format': empty_revision})
    worksheet.write("A2", "lp")
    worksheet.write("B2", "module")
    worksheet.write("C2", "function")
    worksheet.write("D2", "Test Status")
    worksheet.write("E2", "C1")
    worksheet.write("F2", "Test cases")
    worksheet.write("G2", "Number of failed cases")
    worksheet.write("H2", "Failed cases")
    worksheet.write("I2", "Question number")
    worksheet.write("J2", "Description")
    worksheet.write("K2", "Effort [h]")
    return worksheet


def generate_excel_sheet_footer(cell_format_percent, last_raw_number, worksheet):
    # noinspection SpellCheckingInspection
    worksheet.write(last_raw_number + 1, 3, '=COUNTIF(D:D, "finished")/' + str(last_raw_number - 1),
                    cell_format_percent)
    worksheet.write(last_raw_number + 1, 4, '=AVERAGE(E3:' + xl_rowcol_to_cell(last_raw_number, 4) + ')',
                    cell_format_percent)
    worksheet.write(last_raw_number + 1, 5, '=SUM(F3:' + xl_rowcol_to_cell(last_raw_number, 5) + ')')
    worksheet.write(last_raw_number + 1, 6, '=SUM(G3:' + xl_rowcol_to_cell(last_raw_number, 6) + ')')


def apply_conditional_formatting(row, workbook, worksheet):
    status_format_finished = workbook.add_format({'bg_color': 'green'})
    status_format_not_finished = workbook.add_format({'bg_color': 'red'})
    worksheet.conditional_format('D3:' + xl_rowcol_to_cell(row + 2, 3), {'type': 'text',
                                                                         'criteria': 'not containing',
                                                                         'value': 'finished',
                                                                         'format': status_format_not_finished})
    worksheet.conditional_format('D3:' + xl_rowcol_to_cell(row + 2, 3), {'type': 'text',
                                                                         'criteria': 'containing',
                                                                         'value': 'finished',
                                                                         'format': status_format_finished})
    worksheet.conditional_format('G3:' + xl_rowcol_to_cell(row + 2, 6), {'type': 'cell',
                                                                         'criteria': '!=',
                                                                         'value': 0,
                                                                         'format': status_format_not_finished})
    worksheet.conditional_format('G3:' + xl_rowcol_to_cell(row + 2, 6), {'type': 'cell',
                                                                         'criteria': '==',
                                                                         'value': 0,
                                                                         'format': status_format_finished})


def generate_excel_sheet(workbook, data, file):
    worksheet = generate_excel_sheet_header(workbook, file)

    cell_format_percent = workbook.add_format()
    cell_format_percent.set_num_format('0.00%')
    row = 0
    for row, row_data in enumerate(data):
        data = [row+1] + row_data
        worksheet.write_row(row+2, 0, data)  # 2 is header offset from top
        worksheet.data_validation(xl_rowcol_to_cell(row+2, 3), {'validate': 'list',
                                  'source': ['initial', 'in design', 'in testing', 'on hold', 'no test', 'finished']})
        worksheet.write(row+2, 3, "initial")
        worksheet.write(row+2, 4, "", cell_format_percent)

    last_raw_number = row+2
    apply_conditional_formatting(row, workbook, worksheet)
    generate_excel_sheet_footer(cell_format_percent, last_raw_number, worksheet)


def generate_excel_workbook(name, data):
    workbook = xlsxwriter.Workbook(name)
    for sheet_name, values in data:
        generate_excel_sheet(workbook, values, sheet_name)
    workbook.close()
