import traceback

"""


*************
*           *
*           *
*           *
*************

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise  Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height  < 2):
        raise Exception('Widht and height need to be 2 or greater')

    print(symbol * width)

    for i in range(height -2):
        print(symbol + (' '*(width-2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)
boxPrint('O', 5, 15)

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was writen to errror_log.txt')


assert False,'This is the error message'

market_2nd = {'ns':'green','ew':'red'}

def swithchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] == 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] == 'red'
        elif intersection[key] == 'red':
            intersection[key] == 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

swithchLights(market_2nd)