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

    def __init__(self,categories: dict):
        self.categories = categories

    def print_welcome(self):
        print(welcome)
    

    def category_table(self,__nested_list = []) -> int:
        '''Prints an ordered list of self.categories'''
        print('Choose a category;')
        # Checking if function is reoccuring...
        if len(__nested_list) == 0:
            keys = list(self.categories.keys())
            categories = self.categories
        else:
            keys = __nested_list
            categories = __nested_list
        # printing
        for i,c in enumerate(keys,1):
            print(f'\t{i}) {c.title()}')
        # Getting the user input and processing it.
        while True:
            choise = input('SpaceWise: ')
            try:
                choise = int(choise)
                if choise in range(len(categories)+1):
                    if type(categories) is list: # This gets True when function executing 
                        return choise            # a sub-category list
                    elif type(categories[keys[choise-1]]) is list:
                        self.category_table(categories[keys[choise-1]])
                    return choise
                print('[!] Please enter a valid category number.')
            except ValueError:
                print('[!] Please enter an Integer.')

    # TODO: Use threding for animate time taking process like [connectine..., downloading....]
    def run(self):
        self.print_welcome()
        category = self.category_table()
        print('Connnecting...')
        print(self.categories)
        choise = list(self.categories.keys())[category-1].lower()
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