import json
import os.path

def get_locations():
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/locations.json', 'r')
    data = json.load(f)
    f.close()

    locations = []
    for location in data['Results']:
        locations.append([
            f'{location["LocationName"]} - {location["City"]} - {location["Address1"]}',
            location['ServiceId']
        ])

    return locations
