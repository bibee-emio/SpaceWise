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
    

    def category_table(self,__nested_dict:dict = {},url_prefix='') -> str:
        '''Prints an ordered list of self.categories'''
        url_suffix = url_prefix
        print('Choose a category;')
        # Checking if function is reoccuring...
        if len(__nested_dict.keys()) == 0:
            keys = list(self.categories.keys())
            categories = self.categories
        else:
            keys = list(__nested_dict.keys())
            categories = __nested_dict
        # printing
        for i,c in enumerate(keys,1):
            print(f'\t{i}) {c.title()}')
        # Getting the user input and processing it.
        while True:
            choise = input('SpaceWise: ')
            try:
                choise = int(choise)
                #print(keys)
                if choise in range(len(categories)+1):
                    #print(type(categories),categories)
                    if url_prefix:#type(categories) is list:                         # This gets True when function executing 
                        #print(f'{url_suffix}/{categories[keys[choise-1]]}')
                        #return
                        return f'{url_suffix}/{categories[keys[choise-1]]}'    # a sub-category list   for 2nd time 
                    elif type(categories[keys[choise-1]]) is dict:          # for 1st time
                        #print('#######1')
                        return self.category_table(categories[keys[choise-1]],keys[choise-1])
                    url_suffix += keys[choise-1]
                    return url_suffix
                print('[!] Please enter a valid category number.')
            except ValueError:
                print('[!] Please enter an Integer.')

    # TODO: Use threding for animate time taking process like [connectine..., downloading....]
    def run(self):
        self.print_welcome()
        choice = self.category_table().lower()
        #print(choice)
        print('Connnecting...')
        #print(self.categories)
        #choise = list(self.categories.keys())[category-1].lower()
        nasa_space_flight = NasaSpaceFlight(choice)
        header = nasa_space_flight.get_headline()

        print(f'[Latest Article]: {header}')

        if (input('Do you need to download it [y/n]?: ') + ' ')[0].lower() == 'n':
            exit(0)
        
        print('Getting Data...')
        paragraph = nasa_space_flight.get_paragraph()
        print('Downloading Images...')
        urls = nasa_space_flight.get_image_urls()
        # Creating a meaningfull name for image file names
        prefix = f'{choice.title()}-[{paragraph[:10]}]'
        image_count = SpecialFuntions().download_images(urls,prefix)

        document_name = f'{choice.title()}-[{prefix}].docx'.replace('/','-')
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