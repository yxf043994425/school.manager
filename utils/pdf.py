# import pdfkit # 依赖wkhtmltopdf.exe      
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet                      

class DocPDF:
    _doc = None
    _story = None

    def __init__(self, f):
        self._doc = SimpleDocTemplate(f)
        self._story = []

    def append_row(self, t):
        styles = getSampleStyleSheet()
        style = styles['Normal']
        self._story.append(Paragraph(t,style))
    
    def append_table(self, data):
        styles = getSampleStyleSheet()
        style = styles['Normal']
        t = Table(data)
        self._story.append(t)

    def build(self):
        self._doc.build(self._story)