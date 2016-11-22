## David Aldarondo 50177475
import json
import urllib.parse
import urllib.request
##import Project3Outputs

MAPQUEST_API_KEY = 'Fmjtd%7Cluu821uz29%2C25%3Do5-94bnq4&'

BASE_URL = 'http://open.mapquestapi.com/directions/v2/'

def build_url() -> str:
    num = number_of_locations()
    places = locations(num)
    tos = ''
    query_parameters = []
    query_parameters.append(('from', places[0]))
    for i in range(1, len(places)):
        query_parameters.append(('to', places[i]))
    url = BASE_URL + 'route?key=' + MAPQUEST_API_KEY + urllib.parse.urlencode(query_parameters)
    print(url)
    return url


def locations(x: int):
    list_of_locs = []
    for i in range(0, x):
        n = str(input('Location'))
        list_of_locs.append(n)
    return list_of_locs

def number_of_locations():
    num = input('Number of Locations')
    return int(num)

def tos_function(l):
    tos = ''
    for i in range(1, len(l)):
        tos += '&to='
        tos += str(l[i])
    return tos


def get_result(url: str) -> 'json':
    
    '''
    This function takes a URL and returns a Python object representing the
    parsed JSON response.
    '''
    
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()



def print_output(thing: 'data'):
    for i in thing:
        if type(i) != list:
            print(i)
        else:
            print_output(i)
                    

    
