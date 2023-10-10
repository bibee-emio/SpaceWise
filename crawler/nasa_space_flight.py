from datetime import datetime
from typing import List

from . import BeautifulSoup
from . import WebCrawler


class NasaSpaceFlight(WebCrawler):

    def __init__(self,category: str) -> None:
        super().__init__()                                         
        self.__url = 'https://www.nasaspaceflight.com/news/' + category
        #print(self.__url)
        self.get_full_content()    # This makes slow the init... :(                              
        

    # Returns published date of a given article
    # For future implementations
    def get_published_date(self, page: BeautifulSoup) -> datetime:
        published_date = page.p.time['datetime'].split('T')
        dat_e = [int(r) for r in published_date[0].split('-')]
        tim_e = [int(r) for r in published_date[1].split('-')[0].split(':')]
        return datetime(*dat_e,*tim_e)
    
    # self.__url will only show a preview of  the post
    # Getting the full article
    def get_full_content(self) -> BeautifulSoup:
        preview = self.get_soup(self.__url)
        # The URL for full content 
        url = preview.h2.a['href']
        self.__soup_obj = self.get_soup(url)


    
    # Extracting article tags for categorise
    def extract_arctcle_tags(self):...

    # Extracting image URLs of article & return the as a list
    # Example format of returning list => [HEADER_IMAGE,OTHER01,OTHER02,...]
    def get_image_urls(self) -> List[str]:
        # Extracting the post image URL
        post_image = self.__soup_obj.find_all('div',attrs={'class':'post-image'})[0].img['data-src']
        url_list = [post_image]

        # Extracting other images that are related to the article
        for pic in self.__soup_obj.article.find_all('img'):
            if pic.parent.name == 'div':
                url_list.append(pic['src'])
        return url_list

    # Getting the headline(a.k.a. Title) of the article
    def get_headline(self) -> str:
        return self.__soup_obj.h1.get_text()

    # Getting paragraphs of the article
    def get_paragraph(self) -> str:
        full_paragraph = ''
        for para in self.__soup_obj.article.find_all('p'):
            full_paragraph += para.text + '\n'
        #print(full_paragraph) 
        return full_paragraph

    # Print all the infomation to the Document
    def write_doc(self):...
