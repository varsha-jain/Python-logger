import logging
import inspect

def singleton(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls]=cls()
        return instances[cls]
    return get_instance()

@singleton
class Logger():
    @staticmethod
    def log(first, second, passed_result):
        logger = logging.getLogger("exampleApp")
        logger.setLevel(logging.INFO)

        # create the logging file handler
        fh = logging.FileHandler("logged_info.log")

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)

        logger.info("Program started")
        frame, filename, line_number, function_name, lines, index = inspect.stack()[1]

        print(frame, filename, line_number, function_name, lines, index)
        # module = inspect.getmodule(frame[0])

        logger.info("filename is %s: line number is: %s sum of numbers: %s %s is: %s" % (
        filename, line_number, first, second, passed_result))
        logger.info("Done!")


