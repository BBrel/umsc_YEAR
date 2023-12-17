from handlers import labelers
import config
import sys
from loguru import logger
logger.remove()
logger.add(sys.stderr, level="INFO")

for labeler in labelers:
    config.bot.labeler.load(labeler)

if __name__ == '__main__':
    config.bot.run_forever()
