import datetime
import time
import geopandas
import shapely

itc = 0

print("Starting RPSBackend: {0}".format(datetime.datetime.now()))


while(True):
    time.sleep(1)
    print("Itt Count {0}".format(itc))
    itc += 1
