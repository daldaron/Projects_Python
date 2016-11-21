## David Aldarondo 50177475
import Project3JSON
import Project3Outputs

def print_dist(x,y):
    print(y, x, 'miles')
    print()

def print_latlong(x):
    lat = round(float(x[0]),2)
    if str(lat).startswith('-'):
        lat = str(lat) + 'S'
        lat = lat[1:]
    else:
        lat = str(lat) + 'N'
    
    lon = round(float(x[1]),2)
    if str(lon).startswith('-'):
        lon = str(lon) + 'W'
        lon = lon[1:]
    else:
        lon = str(lon) + 'E'
    
    print(lat,lon)
    

def print_time(x,y):
    print(x, round(y[0]/60), 'minutes')
    print()

def print_output(thing: 'data'):
    print()
    for i in range(0,len(thing)):
        n = thing[i]
        other_stuff = []
        try:
            if n == 'Total Distance:':
                print_dist(thing[i+1],n)
            elif n == 'Total Time:':
                print_time(n, thing[i+1])
            elif n == 'DIRECTIONS':
                print(n)
                for x in thing[i+1]:
                    print(x)
                print()
            elif type(thing[i][0]) == tuple:
                for l in range(0,len(thing[i])):
                    print_latlong(thing[i][l])
                print()
        except:
            pass
        else:
            pass
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')


if __name__ == '__main__':
    url = Project3JSON.build_url()
    INFO = Project3JSON.get_result(url)
    data = Project3Outputs.outputs(INFO)
    print_output(data)


