import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 108/data.csv')
weight = df['Weight(Pounds)'].tolist()
graph = ff.create_distplot([weight],['graph for weight'],show_hist=False)
graph.show()