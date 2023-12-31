import sys
import time
import os
import requests
from typing import List


class SpecialFuntions:

    def __init__(self,download_path='src/') -> None:
        self.path = download_path

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
            c += 1
        return c
    
class CliFunctions:
    '''This class mostly functions that are relavent to command line user interface'''

    # Prints given words to the terminal in a type writed way
    @classmethod
    #@staticmethod
    def type_write(cls,word: str):
        for character in word:
            print(character,end='')
            sys.stdout.flush()
            time.sleep(0.05)
        print('')