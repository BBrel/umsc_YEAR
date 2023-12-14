from handlers import labelers
import config

for labeler in labelers:
    config.bot.labeler.load(labeler)

if __name__ == '__main__':
    config.bot.run_forever()
