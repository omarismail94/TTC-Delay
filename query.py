import config
import argparse
from plotter import plotter
import pandas as pd


default = """SELECT date, min_delay AS "sum"
FROM subwaydelays
WHERE min_delay >0
ORDER BY date
"""

parser = argparse.ArgumentParser(description='Query Postgres Database')
parser.add_argument("-q", type=str, help="query statement", default=default)
args = parser.parse_args()

if __name__ == "__main__":
    data = config.query(args.q)
    plotfn = plotter(data)
    plotfn.hist()

