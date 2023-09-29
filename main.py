

from cli import InteractiveCLI
from crawler import NasaSpaceFlight


if __name__=='__main__':
    interactive_cli = InteractiveCLI()
    interactive_cli.print_welcome()

    category =  interactive_cli.category_table()
    '''
    Add a loading with threading for connecting...,downlaoding... etc.
    '''
    print('Connecting...')
    nasa_space_flight = NasaSpaceFlight(interactive_cli.categories[category-1].lower())

    header = nasa_space_flight.get_headline()
    
    print(f'[Latest Article]: {header}')
    if (input('Do you need to download it [y/n]?: ') + ' ')[0].lower() != 'y':
        exit(0)
    print('works')
        
