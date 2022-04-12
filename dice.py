import random
import plotly.figure_factory as ff
diceresult = []
for f in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice1 + dice2
    diceresult.append(result)
graph = ff.create_distplot([diceresult], ['sum of two dices'],show_hist=False)
graph.show()