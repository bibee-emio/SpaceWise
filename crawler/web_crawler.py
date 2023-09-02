
from . import BeautifulSoup,requests


class WebCrawler:
    # Returns the BeautifulSoup object of a given url
    def get_soup(self,url: str) -> BeautifulSoup:
        page = requests.get(url)
        return BeautifulSoup(page.text,'lxml')
    
