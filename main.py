from cli import InteractiveCLI

NASA_SPACE_FLIGHT_CATEGORY_DICTIONARY = {
            'spacex':'',
            'artemis':'',
            'commercial':'',
            'ISS':'',
            'International':[
                'All',
                'Chinese',
                'European',
                'Indian',
                'Russian'
            ],
            'Other':[
                'All',
                'Science',
                'Shuttle',
                'Uncrewed'
            ]
        }

if __name__ == '__main__':
    InteractiveCLI(NASA_SPACE_FLIGHT_CATEGORY_DICTIONARY).run()