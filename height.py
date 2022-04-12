import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 108/data.csv')
height = df['Height(Inches)'].tolist()
graph = ff.create_distplot([height],['graph for height'],show_hist=False)
graph.show()