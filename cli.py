import argparse

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

    def run(self):...
        



if __name__ == '__main__':
    cli1 = InteractiveCLI()
    print(welcome)
    cli1.category_table()