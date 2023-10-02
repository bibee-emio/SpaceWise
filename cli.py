import os

from crawler import NasaSpaceFlight
from helper import SpecialFuntions, NasaSpaceFlightDocumentWriter

welcome = '''
███████╗██████╗  █████╗  ██████╗███████╗██╗    ██╗██╗███████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██║██╔════╝██╔════╝
███████╗██████╔╝███████║██║     █████╗  ██║ █╗ ██║██║███████╗█████╗  
╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝  ██║███╗██║██║╚════██║██╔══╝  
███████║██║     ██║  ██║╚██████╗███████╗╚███╔███╔╝██║███████║███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝
An ideal educational tool for space enthusiasts and students🚀
'''


class InteractiveCLI:

    def __init__(self,
                 categories: list = [
            'spacex',
            'artemis',
            'commercial',
            'ISS'
        ] 
                 ):
        self.categories = categories

    def print_welcome(self):
        print(welcome)


    def category_table(self) -> int:
        print('Choose a category;')
        for i,c in enumerate(self.categories,1):
            print(f'\t{i}) {c.title()}')
        
        while True:
            category = input('SpaceWise: ')
            try:
                category = int(category)
                if category in range(len(self.categories)+1):
                    return category
                print('[!] Please enter a valid category number.')
            except ValueError:
                print('[!] Please enter an Integer.')

    # TODO: Use threding for animate time taking process like [connectine..., downloading....]
    def run(self):
        self.print_welcome()
        category = self.category_table()
        print('Connnecting...')        
        choise = self.categories[category-1].lower()
        nasa_space_flight = NasaSpaceFlight(choise)
        header = nasa_space_flight.get_headline()

        print(f'[Latest Article]: {header}')

        if (input('Do you need to download it [y/n]?: ') + ' ')[0].lower() == 'n':
            exit(0)
        
        print('Getting Data...')
        paragraph = nasa_space_flight.get_paragraph()
        print('Downloading Images...')
        urls = nasa_space_flight.get_image_urls()
        # Creating a meaningfull name for image file names
        prefix = f'{choise.title()}-[{paragraph[:10]}]'
        image_count = SpecialFuntions().download_images(urls,prefix)

        document_name = f'{choise.title()}-[{prefix}].docx'
        # Writing,Adding,Saving the document
        doc = NasaSpaceFlightDocumentWriter(document_name)
        doc.write_document(
            header=header,
            lead_image=f'src/{prefix}-pic-1.jpg',   # Lead image picture number is 1
            paragraph=paragraph,
            image_count=image_count,
            image_prefix=prefix
        )

        print(f'Document Saved to {os.path.abspath(document_name)}')

        



if __name__ == '__main__':
    cli1 = InteractiveCLI()
    print(welcome)
    cli1.category_table()