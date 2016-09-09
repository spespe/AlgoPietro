__author__ = 'Spe'


from pyalgotrade import plotter
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.stratanalyzer import returns
import matplotlib
import sma_crossover

# Load the yahoo feed from the CSV file
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

# Evaluate the strategy with the feed's bars.
myStrategy = sma_crossover.SMACrossOver(feed, "orcl", 20)

# Attach a returns analyzers to the strategy.
returnsAnalyzer = returns.Returns()
myStrategy.attachAnalyzer(returnsAnalyzer)

# Attach the plotter to the strategy.
plt = plotter.StrategyPlotter(myStrategy)
# Include the SMA in the instrument's subplot to get it displayed along with the closing prices.
plt.getInstrumentSubplot("orcl").addDataSeries("SMA", myStrategy.getSMA())
# Plot the simple returns on each bar.
plt.getOrCreateSubplot("returns").addDataSeries("Simple returns", returnsAnalyzer.getReturns())

# Run the strategy.
myStrategy.run()
myStrategy.info("Final portfolio value: $%.2f" % myStrategy.getResult())

# Plot the strategy.
plt.plot()