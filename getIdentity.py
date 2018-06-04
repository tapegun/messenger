import re
import json
import sys

def getIdentity(param):
    thing = ['first_name', 'last_name', 'gender', 'email', 'ip_address']
    with open('/Volumes/PATRIOT/Python/messager/MOCK_DATA.json') as data_file:
        data = json.load(data_file)
        for x in xrange(1, 1000):
            for y in xrange(5):
                piece = data[x][thing[y]]
                if piece == param:
                    return data[x]
    return ("no results..")

