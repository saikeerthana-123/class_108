import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")

fig = ff.create_distplot([df["Mobile Brand"].tolist()], ["Avg Rating"], show_hist=False)
fig.show()