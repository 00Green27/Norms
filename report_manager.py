# coding=utf-8
import xlrd
from xlwt import easyxf
from xlutils.copy import copy
from xlwt.ExcelFormula import Formula
import settings

class ReporterManager:
    row_header_style = easyxf('''
            font: bold on, name Arial;
            border: left thin, right thin, top thin, bottom thin;
            align: wrap on, horiz center, vert center;
            ''')
    name_style = easyxf('''
            font: bold on, name Arial;
            border: bottom thin;
            align: wrap on, horiz center, vert center;
            ''')

    erow_header_style = easyxf('''
            font: bold on, name Arial;
            border: left thin, right thin, top thin, bottom thin;
            align: wrap on;
            ''')

    row_style = easyxf('''
            font: name Arial;
            border: left thin, right thin, top thin, bottom thin;
            align: wrap on;
            ''')

    decimal_row_style = easyxf('''
            font: name Arial;
            border: left thin, right thin, top thin, bottom thin;
            align: wrap on;
            ''', num_format_str='0.00')

    need_style = easyxf('''
            font: bold on, name Arial, colour green;
            border: left thin, right thin, top thin, bottom thin;
            align: wrap on;
            ''')
    retirement_style = easyxf('''
            font: bold on, name Arial, colour red;
            border: left thin, right thin, top thin, bottom thin;
            align: wrap on;
            ''')

    def __init__(self, name):
        rb = xlrd.open_workbook('resources/templates/%s.xlt' % name, on_demand=True, formatting_info=True)
        #rs = rb.sheet_by_index(0)
        self.wb = copy(rb)
        self.ws = self.wb.get_sheet(0)

    def set_department(self, dept):
        self.dept = dept

    def set_current_year(self, year):
        self.ws.write(3, 3, year, self.row_header_style)

    def save(self, filename):
        self.wb.save(filename)

    def write_timesheet(self, data):
        """
        Запись табеля в файл
        """
        self.set_current_year(settings.YEAR)
        if self.dept <> 0:
            self.ws.write(0, 3, self.dept.upper(), self.name_style)

        start_row = 4
        rows = len(data)
        if rows == 0:
            cols = 0
        else:
            cols = len(data[0])

        for r in xrange(rows):
            for c in xrange(cols):
                if c == 3:
                    self.ws.write(r + start_row, c, data[r][c], self.retirement_style)
                elif c == 4:
                    self.ws.write(r + start_row, c, data[r][c], self.need_style)
                elif c < 5:
                    self.ws.write(r + start_row, c, data[r][c], self.row_style)
                elif data[r][c] is not None:
                    self.ws.row(r + start_row).set_cell_number(c, float(data[r][c]), self.decimal_row_style)

        self.ws.write(14, 6, Formula("SUM(G5:G14)"), self.decimal_row_style)
        self.ws.write(14, 7, Formula("SUM(H5:H14)"), self.decimal_row_style)
        self.ws.write(14, 8, Formula("SUM(I5:I14)"), self.decimal_row_style)

    def write_equipment(self, data):
        """
        Запись списка оборудования в файл
        """
        start_row = 21
        row = 0
        rows = len(data)
        rowFix = 0
        hw = 0
        outline_rows = []
        for r in xrange(rows):
            row = r + start_row + rowFix
            if hw <> data[r][6]:
                hw = data[r][6]
                self.ws.write_merge(row, row, 0, 8, data[r][7], self.erow_header_style)
                rowFix += 1
                row += 1
                outline_rows.append(row)
            self.ws.write(row, 0, data[r][0], self.row_style)
            self.ws.write_merge(row, row, 1, 3, data[r][1], self.row_style)
            self.ws.write_merge(row, row, 4, 5, data[r][2], self.row_style)
            self.ws.write(row, 6, data[r][3], self.row_style)
            self.ws.write(row, 7, data[r][4], self.decimal_row_style)
            self.ws.write(row, 8, data[r][5], self.row_style)
            self.ws.row(row).height = 512

        outline_rows.append(row + 1)
        self.outlines(outline_rows)

    def outlines(self, rows):
        """
        Группировка строк по типу оборудования
        """
        for i in xrange(len(rows)):
            if i + 1 >= len(rows):
                break
            for r in xrange(rows[i], rows[i + 1]):
                if r == (rows[i + 1] - 1) and r + 1 <> rows[-1]:
                    continue
                self.ws.row(r).level = 1

    def write_equipments(self, data):
        """
        Создание отчета материально-технической базы
        """
        for row, cols in enumerate(data):
            for col, text in enumerate(cols):
                self.ws.write(row + 2, col, text, self.row_style)

                #rows = len(data) + 3
                #for col in (1, 10):
                #    self.ws.write(rows , col, Formula("SUM(G%dialog:G%dialog)".format(col)), self.decimal_row_style)

        last_row = len(data)+2
        B = 66
        for c in xrange(1, len(data[0])):
            self.ws.write(last_row, c, Formula("SUM({0}3:{0}{1})".format(chr(B), last_row)), self.row_style)
            B += 1