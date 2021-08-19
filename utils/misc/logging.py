from loguru import logger
input()
logger.add(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
           level="DEBUG", 
           colorize=True
)
