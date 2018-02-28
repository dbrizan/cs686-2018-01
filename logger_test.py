from logger import logger


"""
get_logger
Takes logger_type: a string representing type of logger -- 'file' or 'stdout'
Returns a logger instance. May return a ValueError
"""
def get_logger(logger_type, log_level):
    from file_logger import file_logger
    from stdout_logger import stdout_logger

    if logger_type == 'file':
        return file_logger(log_level)
    elif logger_type == 'stdout':
        return stdout_logger(log_level)
    else:
        raise ValueError('Invalid logger type: ' + logger_type)


"""
main
Instantiates and tests two logger types.
"""
if __name__ == '__main__':

    for logger_type in ['file', 'stdout']:
        for log_level in range(4):
            logger = get_logger(logger_type, log_level)

            logger.log(0, 'Starting logger (type = ' + logger_type + ') at log level ' + str(log_level) + '.')
            logger.log(1, 'Important message.')
            logger.log(2, 'Less important message.')
            logger.log(3, 'Not important message.')
            logger.log(0, 'Ending logger.')
