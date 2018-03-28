
import time
from time import gmtime, strftime


while True:
    control = strftime("%S", gmtime())
    print control
    controlb = int(control)

    time.sleep( 1 )
    if controlb == 59:
        print "llegue a 59"
