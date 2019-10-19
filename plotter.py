import matplotlib.pyplot as plt
# import pandas as pd
from fitter import Fitter


class plotter(object):

    def __init__(self,data):
        self.data = data

    def label(self):
        plt.title("Minute Delays per Day")
        plt.xlabel("Day")
        plt.ylabel("Minutes of Delay")
        plt.show()



    def bar(self):
        plt.bar(self.data.ix[:, 0], self.data.ix[:, 1])

    def line(self):
        plt.plot(self.data.ix[:, 0], self.data.ix[:, 1])
        self.label()

    def hist(self):
        plt.title("Histogram with 100 bins")
        plt.xlabel("Minutes of delay")
        plt.ylabel("Number of occurences")

        self.data["sum"].hist(bins=100)
        plt.show()



