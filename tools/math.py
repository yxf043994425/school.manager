import random

from utils import pdf

def init_addition(min, max, count):
    doc = pdf.DocPDF('./output/addition.pdf')

    rows = int(count / 2)
    data = []
    for row in range(rows):
        data.append([random_question(min, max), random_question(min, max)])

    doc.append_table(data)
    doc.build()

def random_question(min, max):
    x = random.randint(min, max)
    y = random.randint(0, max - x)
    return f'{x} + {y} =                               '