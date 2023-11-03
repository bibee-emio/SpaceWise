import os
from threading import Thread

from crawler import NasaSpaceFlight
from helper import SpecialFuntions, NasaSpaceFlightDocumentWriter, CliFunctions

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
                if choise in range(len(categories)+1):
                    if url_prefix:                                              # This gets True when function executing 
                        return f'{url_suffix}/{categories[keys[choise-1]]}'     # a sub-category list   for 2nd time 
                    elif type(categories[keys[choise-1]]) is dict:              # for 1st time
                        return self.category_table(categories[keys[choise-1]],keys[choise-1])
                    url_suffix += keys[choise-1]
                    return url_suffix
                print('[!] Please enter a valid category number.')
            except ValueError:
                print('[!] Please enter an Integer.')

    def run(self):
        self.print_welcome()
        choice = self.category_table().lower()
        #print(choice)

        log_thread_1 = Thread(
            target=CliFunctions.type_write,
            args=['Connecting...']
        )
        log_thread_2 = Thread(
            target=CliFunctions.type_write,
            args=['Getting Data...']
        )
        log_thread_3 = Thread(
            target=CliFunctions.type_write,
            args=['Downloading images...']
        )


        log_thread_1.start()
        nasa_space_flight = NasaSpaceFlight(choice)
        header = nasa_space_flight.get_headline()
        log_thread_1.join()
        print(f'[Latest Article]: {header}')

        if (input('Do you need to download it [y/n]?: ') + ' ')[0].lower() == 'n':
            exit(0)
        
        log_thread_2.start()
        paragraph = nasa_space_flight.get_paragraph()
        log_thread_2.join()
        log_thread_3.start()
        urls = nasa_space_flight.get_image_urls()
        
        # Creating a meaningfull name for image file names
        prefix = f'{choice.title()}-[{paragraph[:10]}]'
        
        image_count = SpecialFuntions().download_images(urls,prefix)
        log_thread_3.join()
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