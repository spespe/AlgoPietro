__author__ = 'Spe'

import itertools
from pyalgotrade.optimizer import local
from pyalgotrade.barfeed import yahoofeed
import RSIpietro


def parameters_generator():
    instrument = ["dia"]
    entrySMA = range(150, 251)
    exitSMA = range(5, 16)
    rsiPeriod = range(2, 11)
    overBoughtThreshold = range(75, 96)
    overSoldThreshold = range(5, 26)
    return itertools.product(instrument, entrySMA, exitSMA, rsiPeriod, overBoughtThreshold, overSoldThreshold)


# The if __name__ == '__main__' part is necessary if running on Windows.
if __name__ == '__main__':
    # Load the feed from the CSV files.
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2000.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2001.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2002.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2003.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2004.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2005.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2006.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2007.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2008.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2009.csv")
    feed.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2010.csv")

    local.run(RSIpietro.RSIpietro, feed, parameters_generator())
