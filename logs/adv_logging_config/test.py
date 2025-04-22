import logging
import logging.config

def setup_logging_from_file():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('file_logger')
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    
setup_logging_from_file()