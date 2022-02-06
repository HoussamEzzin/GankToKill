import coloredlogs, logging


logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)


def menu():
    print("*****GANK TO KILL*****")