import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='myLog.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#the above would write the lgos out to the file vs screen
logging.disable(logging.CRITICAL) #remove this to turn it back on, this would disable critiacal and lower
#logging.disable(logging.DEBUG) would just disable DEBUG and below

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range (1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s ' % (total))
    return  total

print(factorial(5))

#There are 5 levels, debug, info, warning, error, critical

