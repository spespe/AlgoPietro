__author__ = 'Spe'

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma,rsi

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, feed2, instrument, instrument2, smaPeriod, rsiPeriod):
        super(MyStrategy, self).__init__(feed, 1000)
        self.__position = None
        self.__instrument = instrument
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__sma = ma.SMA(feed[instrument].getPriceDataSeries(), smaPeriod)
        self.__rsi = rsi.RSI(feed[instrument].getPriceDataSeries(),rsiPeriod)

    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        self.info("Entered here: BUY at $%.2f" % (execInfo.getPrice()))

    def onExitOk(self, position):
        execInfo = position.getExitOrder().getExecutionInfo()
        self.info("Exited here: SELL at $%.2f" % (execInfo.getPrice()))
        self.__position = None

    def onExitCanceled(self, position):
        # If the exit was canceled, re-submit it.
        self.__position.exitMarket()

    def onEnterCanceled(self, position):
        self.__position = None

    def onBars(self, bars):
        # Wait for enough bars to be available to calculate a SMA.
        if self.__sma[-1] is None:
            return
        elif self.__rsi[-1] is None:
            return

        bar = bars[self.__instrument]
        # If a position was not opened, check if we should enter a long position.
        if self.__position is None:
            if bar.getPrice() < self.__sma[-1] and self.__rsi[-1] > 52:
                # Enter a buy market order for 10 shares. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, 10, True)
        # Check if we have to exit the position.
        elif bar.getPrice() < self.__sma[-1] and not self.__position.exitActive():
            self.__position.exitMarket()


def run_strategy(smaPeriod,rsiPeriod):
    # Load the yahoo feed from the CSV file
    feed2 = yahoofeed.Feed()
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2000.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2001.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2002.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2003.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2004.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2005.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2006.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2007.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2008.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2009.csv")
    feed2.addBarsFromCSV("orcl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\orcl-2010.csv")
    feed=yahoofeed.Feed()
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2000.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2001.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2002.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2003.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2004.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2005.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2006.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2007.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2008.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2009.csv")
    feed.addBarsFromCSV("aapl", "C:\\Users\\Spe\\PycharmProjects\\AlgoPietro\\algoPackage\\data\\aapl-2010.csv")



    # Evaluate the strategy with the feed.
    myStrategy = MyStrategy(feed, feed2, "orcl", "aapl", smaPeriod, rsiPeriod)
    myStrategy.run()
    print "Final portfolio value: $%.2f" % myStrategy.getBroker().getEquity()

run_strategy(50,50)