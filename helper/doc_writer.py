from typing import Union, BinaryIO, List

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.section import _BaseHeaderFooter



class DocumentWriter:

    def __init__(self,output):
        self.__doc = Document()
        self.document_name = output

    # Writing the header of the document
    def write_header(self,heading: str):
        head = self.__doc.add_heading()
        head_run = head.add_run(heading)
        head_run.font.size = Pt(18)
        head_run.font.color.rgb = RGBColor(0,0,0)

    # Writing a paragraph
    def write_paragraph(self,paragraph: str):
        para = self.__doc.add_paragraph()
        para_run = para.add_run(paragraph)
        para_run.font.size = Pt(13)
        para_run.font.name = 'Calibri'
        para_format = para.paragraph_format
        #para_format.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

    # Adding a picture to the document
    def add_image(self,
                  file: Union[str, BinaryIO],
                  width: Union[int, float] = 6,
                  height: Union[int, float] = 4.1):
        self.__doc.add_picture(file,
                               width=Inches(width),
                               height=Inches(height)
            )

    # Save the Document as .docx file
    def save_document(self):
        self.__doc.save(self.document_name)

    
    