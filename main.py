import os
from datetime import datetime
from PIL import Image
from docx.image.exceptions import UnrecognizedImageError

from helper import SpecialFuntions, DocumentWriter
from crawler import NasaSpaceFlight




funcs = SpecialFuntions()
nasa = NasaSpaceFlight()


print('Scraping data...')
header = nasa.get_headline()
paragrph = nasa.get_paragraph()

print('Downloading images...')
urls = nasa.get_image_urls()
images  = funcs.download_images(urls)
doc_name = f'downloads/SpaceX/SpaceX-{datetime.now().date()}.docx'

print('Writing to a document...')
doc = DocumentWriter(doc_name)

doc.write_header(header+'\n')
doc.add_image('src/pic-1.jpg') # Adding the lead image
doc.write_paragraph(paragrph)

# Adding other all remaining images to the end of the document
for i in range(2,images):
    img = f'src/pic-{i}.jpg'
    try:
        doc.add_image(img)
    except UnrecognizedImageError:
        Image.open(img).save(img)
        doc.add_image(img)

doc.save_document()
print(f'Document Saved to {os.path.abspath(doc_name)}')