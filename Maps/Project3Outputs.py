## David Aldarondo 50177475
def outputs(j: 'json'):
    num = int(input())
    data = []
    for i in range(0,num):
        n = str(input())
        if n == 'STEPS':
            n = steps()
            data.append('DIRECTIONS')
            data.append(n.calculate(j))
        elif n == 'TOTALDISTANCE':
            data.append('Total Distance:')
            n = total_distance()
            thing = n.calculate(j)
            data.append(round(thing[0]))
        elif n == 'TOTALTIME':
            data.append('Total Time:')
            n = total_time()
            data.append(n.calculate(j))
        elif n == 'LATLONG':
            n = latlong()
            data.append(n.calculate(j))
    return data

def number_of_outputs():
    num = input()
    return int(num)

class latlong:
    def __init__(self):
        None

    def calculate(self, json_result):
        data = []
        for i in range(0,len(json_result['route']['locations'])):
            data.append((json_result['route']['locations'][i]['latLng']['lat'],
                  json_result['route']['locations'][i]['latLng']['lng']))
        return data

class steps:
    def __init__(self):
        None

    def calculate(self, json_result):
        data = []
        for n in range(0, len(json_result['route']['legs'])):
            for i in range(0, len(json_result['route']['legs'][n]['maneuvers'])):
                data.append(json_result['route']['legs'][n]['maneuvers'][i]['narrative'])
        return data

class total_distance:
    def __init__(self):
        None

    def calculate(self, json_result):
        data = []
        data.append((json_result['route']['distance']))
        return data
        

class total_time:
    def __init__(self):
        None
        
    def calculate(self, json_result):
        data = []
        data.append((json_result['route']['time']))
        return data
