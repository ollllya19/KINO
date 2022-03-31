import openpyxl

from .models import Film


class ExelProcessor:
    def read_exel(self, file):
        book = openpyxl.load_workbook(file)
        sheet = book.active


        k = 10000000
        for i in range(2, sheet.max_row):
            film = Film.objects.create(id = k, photo=sheet[i][1].value, title = sheet[i][2].value,
            year = sheet[i][3].value, certificate = sheet[i][4].value, runtime = sheet[i][5].value,
            genre = sheet[i][6].value, rating = sheet[i][7].value, overview = sheet[i][8].value, director = sheet[i][9].value)
            film.save()
            k += 1
