import numpy as np
import pandas as pd

import yfinance as yf

import plotly.graph_objs as go

data = yf.download(tickers=['OIBR3.SA', 'SAPR4.SA'], period='5d', interval='5m')

print(data)
