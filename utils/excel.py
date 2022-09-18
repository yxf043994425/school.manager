# import xlwings # linux 下使用存在问题
import pandas

class ExcelWings:
    _book = None

    def __init__(self, file):
        self._book = padas.read_excel(file)

    def range(sheet, range):
        return self._book