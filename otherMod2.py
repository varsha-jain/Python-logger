# otherMod2.py
#import logging
import log_config
import otherMod3

#module_logger = logging.getLogger("exampleApp")

 
#----------------------------------------------------------------------
def add(x, y):
    """"""
    #logger = logging.getLogger("exampleApp")
    
    module_logger = log_config.log(x,y,x+y)
    #logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y

def main():
    add(7,8)
    otherMod3.add(4,5)
    
if __name__ == "__main__":
    main()
