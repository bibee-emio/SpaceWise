from cli import InteractiveCLI

NASA_SPACE_FLIGHT_CATEGORY_DICTIONARY = {
            'spacex':'',
            'artemis':'',
            'commercial':'',
            'ISS':'',
            'International':{
                'All':'international',
                'Chinese':'chinese',
                'European':'europe',
                'Indian':'indian',
                'Russian':'russian'
            },
            'Other':{
                'All':'other',
                'Science':'science',
                'Shuttle':'shuttle',
                'Uncrewed':'unmanned'}
        }
        

if __name__ == '__main__':
    InteractiveCLI(NASA_SPACE_FLIGHT_CATEGORY_DICTIONARY).run()