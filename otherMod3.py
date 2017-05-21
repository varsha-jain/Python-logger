#import logging
import log_config
import logging_20thMay

def add(x,y):
    
    #logger = logging.getLogger("exampleApp")
    #module_logger = log_config.log(x,y,x+y)
    module_logger = logging_20thMay.Logger.log(x, y, x + y)
    #logger.info("added %s and %s to get  %s" % (x,y,x+y))
    return x+y

