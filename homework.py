import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 108/data_project.csv')
rating = df['Avg Rating'].tolist()
graph = ff.create_distplot([rating],['Average rating'],show_hist=False)
graph.show()