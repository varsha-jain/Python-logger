#import logging
import log_config

def add(x,y):
    
    #logger = logging.getLogger("exampleApp")
    logger = log_config.log(x,y,x+y)
    #logger.info("added %s and %s to get  %s" % (x,y,x+y))
    return x+y

