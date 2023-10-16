import os
import requests
from typing import List


class SpecialFuntions:

    def __init__(self,download_path='src/') -> None:
        self.path = download_path


    # Spliting the full given paragraph as it easy to
    # write in the document while the page has a Picture
     # TODO: Maybe in the next update
    def split_paragraph(self,full_paragraph: str) -> List[str]:
        ...

    def download_images(self,url_list: List[str],image_prefix):
        c = 1
        for link in url_list:
            data = requests.get(link)

            # Cheking if category folders are exist
            file_name = f'{self.path}{image_prefix}-pic-{c}.jpg'
            file_path = os.path.dirname(file_name)
            if not os.path.exists(file_path):
                os.mkdir(file_path)

            open(file_name,'wb').close()
            with open(f'{self.path}{image_prefix}-pic-{c}.jpg','wb') as imagefile:
                for chunk in data.iter_content(512):
                    imagefile.write(chunk)
                #imagefile.write(data.content)
            #print(f'Image {c} downloaded successfully')
            c += 1
        return c
    

