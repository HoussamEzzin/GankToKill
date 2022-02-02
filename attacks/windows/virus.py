import os

import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s', level='DEBUG', logger=logger)


def shutdown_computer():
    '''
        use cmd to shutdown the computer
    '''
    
    print("shutdown")